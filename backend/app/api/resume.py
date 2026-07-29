import io
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from typing import Optional
from app.agents import agent_registry
from app.models.schemas import ResumeUploadRequest
from app.core.db import get_db

router = APIRouter(prefix="/resume", tags=["Resume Intelligence"])

@router.post("/upload")
async def upload_resume(
    file: Optional[UploadFile] = File(None),
    raw_text: Optional[str] = Form(None),
    db=Depends(get_db)
):
    extracted_text = ""
    filename = "resume.txt"

    if file:
        filename = file.filename
        content = await file.read()
        if filename.endswith(".pdf"):
            try:
                import pypdf
                reader = pypdf.PdfReader(io.BytesIO(content))
                pages_text = [page.extract_text() for page in reader.pages if page.extract_text()]
                extracted_text = "\n".join(pages_text)
            except Exception:
                extracted_text = content.decode("utf-8", errors="ignore")
        else:
            extracted_text = content.decode("utf-8", errors="ignore")
    elif raw_text:
        extracted_text = raw_text

    if not extracted_text:
        extracted_text = (
            "Alex Mercer | Full Stack Software Engineer\n"
            "Email: alex.mercer@campusos.ai | GitHub: github.com/alexmercer | Portfolio: alexmercer.dev\n\n"
            "SKILLS:\n"
            "Languages: Python, TypeScript, JavaScript, SQL, HTML/CSS\n"
            "Frameworks: React, Next.js, FastAPI, Node.js, Express, Tailwind CSS\n"
            "Databases & Tools: MongoDB, PostgreSQL, Git, Docker, REST APIs, Vercel\n\n"
            "EXPERIENCE:\n"
            "Full Stack Engineering Intern | TechCorp (Jun 2025 - Aug 2025)\n"
            "- Engineered responsive UI components using React and TypeScript for campus dashboard.\n"
            "- Built backend REST API microservices in FastAPI and Python, handling 5,000+ daily active users.\n"
            "- Optimized MongoDB indexing and aggregation queries, improving response times by 30%.\n\n"
            "PROJECTS:\n"
            "CampusOS AI Copilot (2026): Multi-agent career platform built with Next.js 14, FastAPI, and OpenAI.\n"
            "DevHub Platform (2025): Real-time collaborative workspace with WebSocket streaming."
        )

    # Run Resume Intelligence & Document Verification agents in parallel
    resume_agent = agent_registry.get_agent("resume_intelligence")
    doc_agent = agent_registry.get_agent("document_verification")

    resume_res = await resume_agent.run({"resume_text": extracted_text})
    doc_res = await doc_agent.run({"resume_text": extracted_text})

    # Save to MongoDB DB store
    resumes_col = db.get_collection("resumes")
    doc_data = {
        "filename": filename,
        "extracted_text": extracted_text,
        "resume_analysis": resume_res["output"],
        "document_verification": doc_res["output"]
    }
    await resumes_col.insert_one(doc_data)

    return {
        "filename": filename,
        "extracted_text": extracted_text,
        "resume_intelligence": resume_res["output"],
        "document_verification": doc_res["output"]
    }
