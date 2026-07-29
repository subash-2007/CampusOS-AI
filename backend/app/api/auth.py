import uuid
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Depends, status, Header
from typing import Optional
from app.models.schemas import UserSignup, UserLogin, TokenResponse, UserProfile
from app.core.security import get_password_hash, verify_password, create_access_token, decode_access_token
from app.core.db import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=TokenResponse)
async def signup(user_in: UserSignup, db=Depends(get_db)):
    users_col = db.get_collection("users")
    existing_user = await users_col.find_one({"email": user_in.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists.")

    user_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc).isoformat()
    user_doc = {
        "_id": user_id,
        "id": user_id,
        "email": user_in.email,
        "password_hash": get_password_hash(user_in.password),
        "full_name": user_in.full_name,
        "target_role": user_in.target_role or "Software Engineer",
        "experience_level": user_in.experience_level or "Entry Level / Student",
        "created_at": now,
        "updated_at": now
    }
    await users_col.insert_one(user_doc)

    profile = UserProfile(
        id=user_id,
        email=user_in.email,
        full_name=user_in.full_name,
        target_role=user_doc["target_role"],
        experience_level=user_doc["experience_level"],
        created_at=now,
        updated_at=now
    )
    token = create_access_token({"sub": user_id, "email": user_in.email})
    return TokenResponse(access_token=token, user=profile)

@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin, db=Depends(get_db)):
    users_col = db.get_collection("users")
    user_doc = await users_col.find_one({"email": credentials.email})
    
    # Instant demo login helper if user is not in database
    if not user_doc and credentials.email == "demo@campusos.ai":
        now = datetime.now(timezone.utc).isoformat()
        user_id = "demo-user-123"
        user_doc = {
            "_id": user_id,
            "id": user_id,
            "email": "demo@campusos.ai",
            "password_hash": get_password_hash("password123"),
            "full_name": "Demo Student",
            "target_role": "Full Stack Software Engineer",
            "experience_level": "Entry Level / Student",
            "created_at": now,
            "updated_at": now
        }
        await users_col.insert_one(user_doc)
    elif not user_doc or not verify_password(credentials.password, user_doc["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    profile = UserProfile(
        id=str(user_doc["_id"]),
        email=user_doc["email"],
        full_name=user_doc.get("full_name", "CampusOS User"),
        target_role=user_doc.get("target_role", "Software Engineer"),
        experience_level=user_doc.get("experience_level", "Student"),
        created_at=user_doc.get("created_at", ""),
        updated_at=user_doc.get("updated_at", "")
    )
    token = create_access_token({"sub": profile.id, "email": profile.email})
    return TokenResponse(access_token=token, user=profile)

@router.get("/me", response_model=UserProfile)
async def get_current_user(authorization: Optional[str] = Header(None), db=Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        # Fallback to demo profile for easy guest testing
        now = datetime.now(timezone.utc).isoformat()
        return UserProfile(
            id="demo-user-123",
            email="demo@campusos.ai",
            full_name="Demo Student",
            target_role="Full Stack Software Engineer",
            experience_level="Entry Level / Student",
            created_at=now,
            updated_at=now
        )
    token = authorization.split(" ")[1]
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    users_col = db.get_collection("users")
    user_doc = await users_col.find_one({"_id": payload.get("sub")})
    if not user_doc:
        now = datetime.now(timezone.utc).isoformat()
        return UserProfile(
            id=payload.get("sub", "user-1"),
            email=payload.get("email", "user@campusos.ai"),
            full_name="CampusOS User",
            target_role="Software Engineer",
            experience_level="Student",
            created_at=now,
            updated_at=now
        )
    return UserProfile(
        id=str(user_doc["_id"]),
        email=user_doc["email"],
        full_name=user_doc.get("full_name", "CampusOS User"),
        target_role=user_doc.get("target_role", "Software Engineer"),
        experience_level=user_doc.get("experience_level", "Student"),
        created_at=user_doc.get("created_at", ""),
        updated_at=user_doc.get("updated_at", "")
    )
