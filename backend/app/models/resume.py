from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class ResumeDB(BaseModel):
    user_id: str
    file_name: str
    file_path: Optional[str] = ""
    extracted_text: str
    skills: List[str] = []
    projects: List[Dict[str, Any]] = []
    education: List[Dict[str, Any]] = []
    experience: List[Dict[str, Any]] = []
    certifications: List[str] = []
    created_at: str

class JobDescriptionDB(BaseModel):
    user_id: str
    company: str
    role: str
    description: str
    created_at: str
