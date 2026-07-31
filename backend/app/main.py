import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.db import db_manager
from app.api import auth, resume, job, agents, chat, analytics, reports, supervisor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CampusOS.Main")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing CampusOS AI Backend Service...")
    await db_manager.connect()
    yield
    logger.info("Shutting down CampusOS AI Backend Service...")
    await db_manager.disconnect()

app = FastAPI(
    title="CampusOS AI - Autonomous Multi-Agent Career Intelligence System",
    description="Enterprise API engine orchestrating 111 Independent Departments and 1,111 specialized AI Agents governed by a central Supervisor Agent.",
    version="2.0.0",
    lifespan=lifespan
)

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root & Health Check Endpoints
@app.get("/")
async def root():
    return {
        "status": "online",
        "app_name": settings.APP_NAME,
        "environment": settings.ENV,
        "db_connected": db_manager.is_connected,
        "departments_available": 111,
        "agents_available": 1111,
        "supervisor_active": True
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": "2026-07-29T08:00:00Z"}

# Include Routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(supervisor.router, prefix="/api/v1")
app.include_router(resume.router, prefix="/api/v1")
app.include_router(job.router, prefix="/api/v1")
app.include_router(agents.router, prefix="/api/v1")
app.include_router(chat.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1")
app.include_router(reports.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
