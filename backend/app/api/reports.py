from datetime import datetime, timezone
from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Optional
from app.database.mongodb import get_mongodb
from app.core.security import decode_access_token
from app.agents.supervisor_agent import supervisor_agent

router = APIRouter(prefix="/reports", tags=["Career Reports & Dashboard Stats"])

@router.get("/latest")
async def get_latest_report(
    authorization: Optional[str] = Header(None),
    mongo=Depends(get_mongodb)
):
    user_id = "guest_user"
    if authorization and authorization.startswith("Bearer "):
        payload = decode_access_token(authorization.split(" ")[1])
        if payload:
            user_id = payload.get("sub", "guest_user")

    reports_col = mongo.get_collection("career_reports")
    report = await reports_col.find_one({"user_id": user_id})
    return report

@router.get("/user/{user_id}")
async def get_user_reports(user_id: str, mongo=Depends(get_mongodb)):
    reports_col = mongo.get_collection("career_reports")
    reports_cursor = reports_col.find({"user_id": user_id})
    results = await reports_cursor.to_list(length=20)
    return results

@router.post("/generate")
async def generate_full_report(
    resume_text: str = "",
    target_role: str = "Full Stack Software Engineer",
    authorization: Optional[str] = Header(None),
    mongo=Depends(get_mongodb)
):
    user_id = "guest_user"
    if authorization and authorization.startswith("Bearer "):
        payload = decode_access_token(authorization.split(" ")[1])
        if payload:
            user_id = payload.get("sub", "guest_user")

    report = await supervisor_agent.run_supervisor_pipeline(
        user_id=user_id,
        resume_text=resume_text,
        target_role=target_role,
        db=mongo
    )

    return report
