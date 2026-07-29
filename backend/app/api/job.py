import uuid
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, Header
from typing import Optional
from app.database.mongodb import get_mongodb
from app.core.security import decode_access_token
from app.nlp import extract_skills_from_text

router = APIRouter(prefix="/job", tags=["Job Description Management"])


@router.post("/analyze")
async def analyze_job(
    company: str = "Tech Enterprise",
    role: str = "Software Engineer",
    description: str = "",
    authorization: Optional[str] = Header(None),
    mongo=Depends(get_mongodb)
):
    user_id = "guest_user"
    if authorization and authorization.startswith("Bearer "):
        payload = decode_access_token(authorization.split(" ")[1])
        if payload:
            user_id = payload.get("sub", "guest_user")

    now = datetime.now(timezone.utc).isoformat()
    job_id = str(uuid.uuid4())

    job_doc = {
        "_id": job_id,
        "job_id": job_id,
        "user_id": user_id,
        "company": company,
        "role": role,
        "description": description,
        "created_at": now
    }

    jobs_col = mongo.get_collection("job_descriptions")
    await jobs_col.insert_one(job_doc)

    skills = extract_skills_from_text(description)

    return {
        "job_id": job_id,
        "company": company,
        "role": role,
        "description": description,
        "extracted_skills": skills,
        "created_at": now
    }


@router.post("/match")
async def match_job(
    resume_text: str = "",
    job_description_text: str = "",
    mongo=Depends(get_mongodb)
):
    from app.nlp import compute_ats_optimization
    ats_res = compute_ats_optimization(resume_text, job_description_text)
    return {"ats_optimization": ats_res}
