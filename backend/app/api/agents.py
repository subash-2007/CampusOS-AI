from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any
from app.agents import agent_registry
from app.models.schemas import AgentRunRequest, AgentRunResponse
from datetime import datetime, timezone

router = APIRouter(prefix="/agents", tags=["AI Agents Hub"])

@router.get("/list")
async def list_agents():
    return agent_registry.list_agents()

@router.post("/run/{agent_id}", response_model=AgentRunResponse)
async def run_agent(agent_id: str, request: AgentRunRequest):
    agent = agent_registry.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail=f"Agent '{agent_id}' not found.")

    inputs = {
        "prompt": request.prompt or "",
        "resume_text": request.resume_text or "",
        "job_description_text": request.job_description_text or "",
        **(request.parameters or {})
    }

    res = await agent.run(inputs)
    now = datetime.now(timezone.utc).isoformat()

    return AgentRunResponse(
        agent_id=agent.agent_id,
        agent_name=agent.name,
        status="success",
        timestamp=now,
        reasoning_steps=res.get("reasoning_steps", []),
        output=res.get("output", {})
    )
