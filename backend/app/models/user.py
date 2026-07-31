from pydantic import BaseModel
from typing import Optional

class UserRegister(BaseModel):
    name: str
    email: str
    password: str
    target_role: Optional[str] = "Software Engineer"
    experience: Optional[str] = "Entry Level / Student"
    career_goal: Optional[str] = "Land a high-impact software engineering role"

class UserLogin(BaseModel):
    email: str
    password: str

class UserProfile(BaseModel):
    id: str
    name: str
    email: str
    target_role: str
    experience: str
    career_goal: Optional[str] = "Software Engineer"
    created_at: str

class UserTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserProfile
