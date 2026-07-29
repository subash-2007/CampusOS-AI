from fastapi import APIRouter, Depends
from app.models.schemas import JobDescriptionRequest, ATSMatchRequest
from app.agents import agent_registry
from app.core.db import get_db

router = APIRouter(prefix="/job", tags=["Job & ATS Intelligence"])

@router.post("/analyze")
async def analyze_job(req: JobDescriptionRequest, db=Depends(get_db)):
    job_agent = agent_registry.get_agent("job_intelligence")
    company_agent = agent_registry.get_agent("company_intelligence")

    job_res = await job_agent.run({"job_description_text": req.description_text})
    company_res = await company_agent.run({"company_name": req.company or "Tech Enterprise"})

    return {
        "job_analysis": job_res["output"],
        "company_intelligence": company_res["output"]
    }

@router.post("/match")
async def match_resume_to_job(req: ATSMatchRequest, db=Depends(get_db)):
    ats_agent = agent_registry.get_agent("ats_optimization")
    skill_agent = agent_registry.get_agent("skill_gap_intelligence")

    ats_res = await ats_agent.run({
        "resume_text": req.resume_text,
        "job_description_text": req.job_description_text
    })

    skill_res = await skill_agent.run({
        "resume_text": req.resume_text,
        "target_role": "Target Job Posting"
    })

    return {
        "ats_optimization": ats_res["output"],
        "skill_gap_analysis": skill_res["output"]
    }
