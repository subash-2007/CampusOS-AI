from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from typing import Optional
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
    db=Depends(get_db)
):
    """Executes full autonomous multi-agent Supervisor pipeline on candidate inputs."""
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
        company_name=company_name
    )

    # Save to MongoDB database store
    reports_col = db.get_collection("supervisor_reports")
    await reports_col.insert_one(report)

    return report
