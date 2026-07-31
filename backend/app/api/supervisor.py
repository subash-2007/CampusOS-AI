from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException, Body
from typing import Optional, Dict, Any
from app.agents.supervisor_agent import supervisor_agent
from app.core.db import get_db

router = APIRouter(prefix="/supervisor", tags=["Supervisor Agent Manager"])

@router.post("/analyze")
async def analyze_career_intelligence(
    resume_file: Optional[UploadFile] = File(None),
    resume_text: Optional[str] = Form(None),
    job_file: Optional[UploadFile] = File(None),
    job_text: Optional[str] = Form(None),
    job_url: Optional[str] = Form(None),
    career_goal: Optional[str] = Form(None),
    target_role: Optional[str] = Form(None),
    experience_level: Optional[str] = Form(None),
    company_name: Optional[str] = Form(None),
    user_id: Optional[str] = Form(None),
    db=Depends(get_db)
):
    """Executes full autonomous multi-agent Supervisor pipeline across all 28 AI Agents on candidate inputs."""
    resume_bytes = None
    resume_filename = None
    if resume_file:
        resume_bytes = await resume_file.read()
        resume_filename = resume_file.filename

    job_bytes = None
    job_filename = None
    if job_file:
        job_bytes = await job_file.read()
        job_filename = job_file.filename

    report = await supervisor_agent.run_supervisor_pipeline(
        user_id=user_id or "guest_user",
        resume_filename=resume_filename,
        resume_bytes=resume_bytes,
        resume_text=resume_text,
        job_filename=job_filename,
        job_bytes=job_bytes,
        job_text=job_text,
        job_url=job_url,
        career_goal=career_goal,
        target_role=target_role,
        experience_level=experience_level,
        company_name=company_name,
        db=db
    )

    return report

@router.post("/analyze-json")
async def analyze_career_intelligence_json(
    payload: Dict[str, Any] = Body(...),
    db=Depends(get_db)
):
    """JSON body endpoint for multi-agent pipeline execution."""
    report = await supervisor_agent.run_supervisor_pipeline(
        user_id=payload.get("user_id") or "guest_user",
        resume_text=payload.get("resume_text"),
        job_text=payload.get("job_description_text") or payload.get("job_text"),
        job_url=payload.get("job_url"),
        career_goal=payload.get("career_goal"),
        target_role=payload.get("target_role"),
        experience_level=payload.get("experience_level"),
        company_name=payload.get("company_name"),
        db=db
    )
    return report

@router.get("/session/{session_id}/status")
async def get_session_status(session_id: str, db=Depends(get_db)):
    """Polls real-time progress for an active analysis session in MongoDB."""
    sessions_col = db.get_collection("analysis_sessions")
    session = await sessions_col.find_one({"_id": session_id})
    if not session:
        session = await sessions_col.find_one({"session_id": session_id})
    
    if not session:
        return {"session_id": session_id, "status": "processing", "progress_pct": 50, "completed_agents": []}
    
    # Clean Mongo ObjectId before returning
    if "_id" in session:
        session["_id"] = str(session["_id"])

    return session

@router.get("/latest-report")
async def get_latest_report(user_id: Optional[str] = "guest_user", db=Depends(get_db)):
    """Retrieves the candidate's latest career report from MongoDB."""
    reports_col = db.get_collection("career_reports")
    report = await reports_col.find_one({"user_id": user_id}, sort=[("created_at", -1)])
    if not report:
        report = await reports_col.find_one({}, sort=[("created_at", -1)])
    
    if report and "_id" in report:
        report["_id"] = str(report["_id"])
    return report
