import uuid
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Depends, Header
from typing import Optional, Dict, Any
from pydantic import BaseModel
from app.agents.supervisor_agent import supervisor_agent
from app.agents.registry import agent_registry
from app.database.mongodb import get_mongodb
from app.core.security import decode_access_token

router = APIRouter(prefix="/agents", tags=["AI Agents System & Analysis"])


class RunAnalysisRequest(BaseModel):
    """Direct inline request - carries resume_text and jd_text so we skip the MongoDB round-trip lookup."""
    user_id: Optional[str] = None
    # Inline content (preferred path — avoids MongoDB ID lookup race conditions)
    resume_text: Optional[str] = ""
    job_description_text: Optional[str] = ""
    target_role: Optional[str] = "Software Engineer"
    company_name: Optional[str] = "Target Enterprise"
    experience_level: Optional[str] = "Student"
    career_goal: Optional[str] = ""
    # Legacy ID-based lookup (kept for backward compat)
    resume_id: Optional[str] = None
    job_id: Optional[str] = None


@router.get("/list")
async def list_agents():
    return agent_registry.list_agents()


@router.get("/departments")
async def list_departments():
    return {
        "departments_count": len(agent_registry.list_departments()),
        "agents_count": len(agent_registry.list_agents()),
        "departments": agent_registry.list_departments()
    }


@router.post("/run-analysis")
async def run_multi_agent_analysis(
    req: RunAnalysisRequest,
    authorization: Optional[str] = Header(None),
    mongo=Depends(get_mongodb)
):
    """
    Main 14-agent supervisor pipeline entry point.

    Accepts inline resume_text + job_description_text directly to avoid
    MongoDB ID lookup round-trips that could silently fail.

    Also falls back to MongoDB ID lookup for backward compatibility.
    """
    user_id = req.user_id or "guest_user"
    if authorization and authorization.startswith("Bearer "):
        payload = decode_access_token(authorization.split(" ")[1])
        if payload:
            user_id = payload.get("sub", user_id)

    resume_text = req.resume_text or ""
    job_text = req.job_description_text or ""

    # Fallback: look up by ID if inline text not provided
    if not resume_text and req.resume_id:
        resumes_col = mongo.get_collection("resumes")
        resume_doc = await resumes_col.find_one({"_id": req.resume_id})
        if not resume_doc:
            resume_doc = await resumes_col.find_one({"resume_id": req.resume_id})
        if not resume_doc:
            resume_doc = await resumes_col.find_one({"user_id": user_id})
        if resume_doc:
            resume_text = resume_doc.get("extracted_text", "")

    if not job_text and req.job_id:
        jobs_col = mongo.get_collection("job_descriptions")
        job_doc = await jobs_col.find_one({"_id": req.job_id})
        if not job_doc:
            job_doc = await jobs_col.find_one({"job_id": req.job_id})
        if not job_doc:
            job_doc = await jobs_col.find_one({"user_id": user_id})
        if job_doc:
            job_text = job_doc.get("description", "")

    company_name = req.company_name or "Target Enterprise"
    target_role = req.target_role or "Software Engineer"

    # Run Supervisor Agent Pipeline
    report = await supervisor_agent.run_supervisor_pipeline(
        user_id=user_id,
        resume_text=resume_text,
        job_text=job_text,
        company_name=company_name,
        target_role=target_role,
        experience_level=req.experience_level or "Student",
        career_goal=req.career_goal or f"Land a role as {target_role}",
        db=mongo
    )

    return {
        "status": "completed",
        "analysis_id": report.get("report_id", str(uuid.uuid4())),
        "user_id": user_id,
        **report
    }


@router.get("/results/{analysis_id}")
async def get_analysis_result(
    analysis_id: str,
    authorization: Optional[str] = Header(None),
    mongo=Depends(get_mongodb)
):
    """Fetch a previously completed analysis from MongoDB by analysis_id (fallback for page refreshes)."""
    user_id = "guest_user"
    if authorization and authorization.startswith("Bearer "):
        payload = decode_access_token(authorization.split(" ")[1])
        if payload:
            user_id = payload.get("sub", "guest_user")

    reports_col = mongo.get_collection("career_reports")
    report = await reports_col.find_one({"report_id": analysis_id, "user_id": user_id})
    if not report:
        report = await reports_col.find_one({"report_id": analysis_id})
    if not report:
        report = await reports_col.find_one({"session_id": analysis_id})
    if not report:
        raise HTTPException(status_code=404, detail="Analysis result not found.")
    return report


def _normalize_agent_keys(agent_id: str) -> list:
    """Returns all possible database key representations for a given agent_id slug."""
    clean = agent_id.replace("-", "_")
    keys = [agent_id, clean]
    synonyms = {
        "skill_gap": "skill_gap_intelligence",
        "skill_gap_intelligence": "skill_gap",
        "interview": "interview_intelligence",
        "interview_intelligence": "interview",
        "portfolio": "portfolio_intelligence",
        "portfolio_intelligence": "portfolio",
        "communication": "communication_intelligence",
        "communication_intelligence": "communication",
        "memory": "memory_personalization",
        "memory_personalization": "memory",
        "supervisor": "supervisor_evaluation",
        "supervisor_evaluation": "supervisor"
    }
    if clean in synonyms:
        keys.append(synonyms[clean])
    return list(dict.fromkeys(keys))


@router.get("/session/{session_id}/agent/{agent_id}")
async def get_session_agent_output(
    session_id: str,
    agent_id: str,
    mongo=Depends(get_mongodb)
):
    """Fetch specific agent output from MongoDB agent_outputs collection by session_id + agent_id."""
    outputs_col = mongo.get_collection("agent_outputs")
    possible_keys = _normalize_agent_keys(agent_id)
    
    output_doc = await outputs_col.find_one({"session_id": session_id, "agent_id": {"$in": possible_keys}})
    if not output_doc:
        output_doc = await outputs_col.find_one({"agent_id": {"$in": possible_keys}})
    if not output_doc:
        # Fallback to report document
        reports_col = mongo.get_collection("career_reports")
        rep = await reports_col.find_one({"session_id": session_id})
        if rep and "agents" in rep:
            for k in possible_keys:
                if k in rep["agents"]:
                    return {
                        "session_id": session_id,
                        "agent_id": agent_id,
                        "response": rep["agents"][k],
                        "status": "completed"
                    }
        raise HTTPException(status_code=404, detail=f"Output for agent '{agent_id}' not found in session '{session_id}'.")
    output_doc["_id"] = str(output_doc["_id"])
    return output_doc


@router.get("/latest/agent/{agent_id}")
async def get_latest_agent_output(
    agent_id: str,
    authorization: Optional[str] = Header(None),
    mongo=Depends(get_mongodb)
):
    """Fetch the latest output for a given agent_id for the current logged-in user."""
    user_id = "guest_user"
    if authorization and authorization.startswith("Bearer "):
        payload = decode_access_token(authorization.split(" ")[1])
        if payload:
            user_id = payload.get("sub", "guest_user")

    outputs_col = mongo.get_collection("agent_outputs")
    possible_keys = _normalize_agent_keys(agent_id)
    output_doc = None
    try:
        output_doc = await outputs_col.find_one({"agent_id": {"$in": possible_keys}}, sort=[("timestamp", -1)])
    except TypeError:
        # Fallback for InMemoryCollection or test mocks
        cursor = outputs_col.find({"agent_id": {"$in": possible_keys}})
        if hasattr(cursor, "to_list"):
            docs = await cursor.to_list(length=100)
        elif hasattr(cursor, "__await__"):
            docs = await cursor
        else:
            docs = list(cursor)
        if docs:
            docs = sorted(docs, key=lambda x: str(x.get("timestamp", "")), reverse=True)
            output_doc = docs[0]

    if not output_doc:
        reports_col = mongo.get_collection("career_reports")
        rep = None
        try:
            rep = await reports_col.find_one({"user_id": user_id}, sort=[("created_at", -1)])
        except TypeError:
            rep = await reports_col.find_one({"user_id": user_id})
        if not rep:
            try:
                rep = await reports_col.find_one({}, sort=[("created_at", -1)])
            except TypeError:
                rep = await reports_col.find_one({})

        if rep and "agents" in rep:
            for k in possible_keys:
                if k in rep["agents"]:
                    return {
                        "session_id": rep.get("session_id", "active_session"),
                        "agent_id": agent_id,
                        "response": rep["agents"][k],
                        "status": "completed"
                    }
        raise HTTPException(status_code=404, detail=f"No output found for agent '{agent_id}'.")
    output_doc["_id"] = str(output_doc["_id"])
    return output_doc


@router.post("/run/{agent_id}")
async def run_single_agent(agent_id: str, request_data: Dict[str, Any]):
    agent = agent_registry.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail=f"Agent '{agent_id}' not found.")

    tool_trace = await agent.execute_autonomous_tools(request_data)
    res = await agent.run(request_data)
    now = datetime.now(timezone.utc).isoformat()

    return {
        "agent_id": agent.agent_id,
        "agent_name": agent.name,
        "status": "success",
        "timestamp": now,
        "goal": getattr(agent, "description", "Autonomous agentic analysis"),
        "tools_used": tool_trace.get("tools_used", ["LLM Reasoning Engine"]),
        "decisions_made": tool_trace.get("decisions_made", []),
        "confidence_score": tool_trace.get("confidence_score", 90),
        "reasoning_steps": res.get("reasoning_steps", []),
        "output": res.get("output", res)
    }
