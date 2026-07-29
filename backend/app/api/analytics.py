from fastapi import APIRouter, Depends
from app.agents import agent_registry
from app.core.db import get_db

router = APIRouter(prefix="/analytics", tags=["Career Analytics"])

@router.get("/overview")
async def get_analytics_overview(db=Depends(get_db)):
    analytics_agent = agent_registry.get_agent("career_analytics")
    market_agent = agent_registry.get_agent("market_trend")

    analytics_res = await analytics_agent.run({})
    market_res = await market_agent.run({"domain": "Full Stack Software Engineering"})

    return {
        "analytics": analytics_res["output"],
        "market_trends": market_res["output"]
    }
