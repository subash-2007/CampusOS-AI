from datetime import datetime, timezone
from fastapi import APIRouter, Depends
from app.models.schemas import ChatSessionRequest, ChatMessage
from app.agents import agent_registry
from app.core.db import get_db

router = APIRouter(prefix="/chat", tags=["Multi-Agent Chat Command Center"])

@router.post("/message", response_model=ChatMessage)
async def send_chat_message(req: ChatSessionRequest, db=Depends(get_db)):
    selected_agent_id = req.selected_agent or "career_orchestrator"
    agent = agent_registry.get_agent(selected_agent_id)

    res = await agent.run({
        "prompt": req.message,
        "context": req.context or {}
    })

    now = datetime.now(timezone.utc).isoformat()
    output = res.get("output", {})
    
    # Format message response text nicely from output object
    if "response" in output:
        text = str(output["response"])
    elif "overall_score" in output:
        text = f"Analyzed Resume! Overall Score: **{output['overall_score']}/100**. Strengths: {', '.join(output.get('strengths', []))}"
    elif "match_score" in output:
        text = f"ATS Match Score: **{output['match_score']}%**. Matched Keywords: {', '.join(output.get('matched_keywords', []))}"
    elif "technical_questions" in output:
        q = output["technical_questions"][0]["question"] if output.get("technical_questions") else "Walk me through your recent project."
        text = f"Interview Prep Question: **{q}**"
    elif "subject_line" in output:
        text = f"Cold Email Draft:\n**Subject**: {output.get('subject_line')}\n\n{output.get('body_text')}"
    else:
        text = f"Agent **{agent.name}** processed your request successfully."

    msg = ChatMessage(
        sender=agent.agent_id,
        text=text,
        agent_id=agent.agent_id,
        timestamp=now,
        reasoning=res.get("reasoning_steps", []),
        metadata=output
    )

    # Save message to DB store
    chats_col = db.get_collection("chat_history")
    await chats_col.insert_one(msg.model_dump())

    return msg
