import uuid
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Depends, Header
from typing import Optional
from app.models.user import UserRegister, UserLogin, UserTokenResponse, UserProfile
from app.core.security import get_password_hash, verify_password, create_access_token, decode_access_token
from app.database.mongodb import get_mongodb

router = APIRouter(prefix="/auth", tags=["User Authentication"])

@router.post("/register", response_model=UserTokenResponse)
@router.post("/signup", response_model=UserTokenResponse)
async def register(user_in: UserRegister, mongo=Depends(get_mongodb)):
    users_col = mongo.get_collection("users")
    existing_user = await users_col.find_one({"email": user_in.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists.")

    user_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc).isoformat()
    
    user_doc = {
        "_id": user_id,
        "id": user_id,
        "name": user_in.name,
        "full_name": user_in.name,
        "email": user_in.email,
        "password_hash": get_password_hash(user_in.password),
        "target_role": user_in.target_role or "Full Stack Software Engineer",
        "experience": user_in.experience or "Student",
        "career_goal": user_in.career_goal or f"Land a role as {user_in.target_role}",
        "created_at": now
    }
    await users_col.insert_one(user_doc)

    profile = UserProfile(
        id=user_id,
        name=user_in.name,
        email=user_in.email,
        target_role=user_doc["target_role"],
        experience=user_doc["experience"],
        career_goal=user_doc["career_goal"],
        created_at=now
    )
    token = create_access_token({"sub": user_id, "email": user_in.email})
    return UserTokenResponse(access_token=token, user=profile)

@router.post("/login", response_model=UserTokenResponse)
async def login(credentials: UserLogin, mongo=Depends(get_mongodb)):
    users_col = mongo.get_collection("users")
    user_doc = await users_col.find_one({"email": credentials.email})
    
    if not user_doc or not verify_password(credentials.password, user_doc.get("password_hash", "")):
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    user_id = str(user_doc.get("_id") or user_doc.get("id"))
    profile = UserProfile(
        id=user_id,
        name=user_doc.get("name", user_doc.get("full_name", "User")),
        email=user_doc["email"],
        target_role=user_doc.get("target_role", "Software Engineer"),
        experience=user_doc.get("experience", "Student"),
        career_goal=user_doc.get("career_goal", "Software Engineer"),
        created_at=user_doc.get("created_at", "")
    )
    token = create_access_token({"sub": user_id, "email": profile.email})
    return UserTokenResponse(access_token=token, user=profile)

@router.get("/me", response_model=UserProfile)
async def get_current_user(authorization: Optional[str] = Header(None), mongo=Depends(get_mongodb)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    token = authorization.split(" ")[1]
    payload = decode_access_token(token)
    if not payload or not payload.get("sub"):
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    
    user_id = payload.get("sub")
    users_col = mongo.get_collection("users")
    user_doc = await users_col.find_one({"_id": user_id})
    if not user_doc:
        user_doc = await users_col.find_one({"id": user_id})
    
    if not user_doc:
        raise HTTPException(status_code=404, detail="User profile not found in MongoDB")

    return UserProfile(
        id=str(user_doc.get("_id") or user_doc.get("id")),
        name=user_doc.get("name", user_doc.get("full_name", "CampusOS Candidate")),
        email=user_doc["email"],
        target_role=user_doc.get("target_role", "Software Engineer"),
        experience=user_doc.get("experience", "Student"),
        career_goal=user_doc.get("career_goal", "Software Engineer"),
        created_at=user_doc.get("created_at", "")
    )
