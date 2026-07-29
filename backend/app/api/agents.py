from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Depends, Header
from typing import Optional, Dict, Any
from app.models.report import AgentRunAnalysisRequest
from app.agents.supervisor_agent import supervisor_agent
from app.agents.registry import agent_registry
from app.database.mongodb import get_mongodb
from app.core.security import decode_access_token

router = APIRouter(prefix="/agents", tags=["AI Agents System & Analysis"])

@router.get("/list")
async def list_agents():
    return agent_registry.list_agents()

@router.post("/run-analysis")
async def run_multi_agent_analysis(
    req: AgentRunAnalysisRequest,
    authorization: Optional[str] = Header(None),
    mongo=Depends(get_mongodb)
):
    user_id = req.user_id or "guest_user"
    if authorization and authorization.startswith("Bearer "):
        payload = decode_access_token(authorization.split(" ")[1])
        if payload:
            user_id = payload.get("sub", user_id)

    # 1. Fetch Resume Document from MongoDB resumes collection
    resumes_col = mongo.get_collection("resumes")
    resume_doc = None
    if req.resume_id:
        resume_doc = await resumes_col.find_one({"_id": req.resume_id})
    if not resume_doc:
        resume_doc = await resumes_col.find_one({"user_id": user_id})

    resume_text = resume_doc.get("extracted_text", "") if resume_doc else ""

    # 2. Fetch Job Description Document from MongoDB job_descriptions collection
    jobs_col = mongo.get_collection("job_descriptions")
    job_doc = None
    if req.job_id:
        job_doc = await jobs_col.find_one({"_id": req.job_id})
    if not job_doc:
        job_doc = await jobs_col.find_one({"user_id": user_id})

    job_text = job_doc.get("description", "") if job_doc else ""
    company_name = req.company_name or (job_doc.get("company", "Target Enterprise") if job_doc else "Target Enterprise")
    target_role = req.target_role or (job_doc.get("role", "Software Engineer") if job_doc else "Software Engineer")

    # 3. Run Supervisor Agent Pipeline & Store in MongoDB agent_results and career_reports
    report = await supervisor_agent.run_supervisor_pipeline(
        user_id=user_id,
        resume_text=resume_text,
        job_text=job_text,
        company_name=company_name,
        target_role=target_role,
        db=mongo
    )

    return report

@router.post("/run/{agent_id}")
async def run_single_agent(agent_id: str, request_data: Dict[str, Any]):
    agent = agent_registry.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail=f"Agent '{agent_id}' not found.")

    res = await agent.run(request_data)
    now = datetime.now(timezone.utc).isoformat()

    return {
        "agent_id": agent.agent_id,
        "agent_name": agent.name,
        "status": "success",
        "timestamp": now,
        "reasoning_steps": res.get("reasoning_steps", []),
        "output": res.get("output", {})
    }
