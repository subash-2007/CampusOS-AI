import uuid
import io
from datetime import datetime, timezone
from fastapi import APIRouter, UploadFile, File, Form, Depends, Header
from typing import Optional
from app.nlp import parse_document_input, extract_skills_from_text, analyze_resume_dynamically
from app.database.mongodb import get_mongodb
from app.core.security import decode_access_token

router = APIRouter(prefix="/resume", tags=["Resume Management"])

@router.post("/upload")
async def upload_resume(
    file: Optional[UploadFile] = File(None),
    raw_text: Optional[str] = Form(None),
    authorization: Optional[str] = Header(None),
    mongo=Depends(get_mongodb)
):
    user_id = "guest_user"
    if authorization and authorization.startswith("Bearer "):
        payload = decode_access_token(authorization.split(" ")[1])
        if payload:
            user_id = payload.get("sub", "guest_user")

    file_bytes = None
    filename = "resume.txt"
    if file:
        filename = file.filename
        file_bytes = await file.read()

    extracted_text = parse_document_input(filename, file_bytes, raw_text)
    if not extracted_text:
        extracted_text = "Sample Resume text submitted for student candidate."

    # Dynamic Analysis
    analysis = analyze_resume_dynamically(extracted_text)
    skills = extract_skills_from_text(extracted_text)

    now = datetime.now(timezone.utc).isoformat()
    resume_id = str(uuid.uuid4())

    resume_doc = {
        "_id": resume_id,
        "resume_id": resume_id,
        "user_id": user_id,
        "file_name": filename,
        "file_path": f"/uploads/{filename}",
        "extracted_text": extracted_text,
        "skills": skills,
        "projects": [{"title": "Sample Project", "description": "Full stack web app"}],
        "education": [{"degree": "Bachelor of Science", "field": "Computer Science"}],
        "experience": [{"title": "Software Intern", "company": "Tech Corp"}],
        "created_at": now,
        "resume_analysis": analysis
    }

    resumes_col = mongo.get_collection("resumes")
    await resumes_col.insert_one(resume_doc)

    return {
        "resume_id": resume_id,
        "file_name": filename,
        "extracted_text": extracted_text,
        "skills": skills,
        "resume_intelligence": analysis
    }
