from datetime import datetime, timezone
from fastapi import APIRouter, Depends
from app.agents import agent_registry
from app.core.db import get_db

router = APIRouter(prefix="/reports", tags=["AI Comprehensive Reports"])

@router.post("/generate")
async def generate_full_report(resume_text: str = "", target_role: str = "Full Stack Engineer", db=Depends(get_db)):
    now = datetime.now(timezone.utc).isoformat()

    # Run agents to construct full report
    resume_agent = agent_registry.get_agent("resume_intelligence")
    ats_agent = agent_registry.get_agent("ats_optimization")
    job_agent = agent_registry.get_agent("job_intelligence")
    company_agent = agent_registry.get_agent("company_intelligence")
    skill_agent = agent_registry.get_agent("skill_gap_intelligence")
    roadmap_agent = agent_registry.get_agent("career_roadmap")
    market_agent = agent_registry.get_agent("market_trend")
    portfolio_agent = agent_registry.get_agent("portfolio_intelligence")

    r_out = await resume_agent.run({"resume_text": resume_text})
    a_out = await ats_agent.run({"resume_text": resume_text, "job_description_text": target_role})
    j_out = await job_agent.run({"job_description_text": target_role})
    c_out = await company_agent.run({"company_name": "Target Enterprise"})
    s_out = await skill_agent.run({"resume_text": resume_text, "target_role": target_role})
    rm_out = await roadmap_agent.run({"target_role": target_role})
    m_out = await market_agent.run({"domain": target_role})
    p_out = await portfolio_agent.run({"target_role": target_role})

    report_doc = {
        "report_id": f"REP-{int(datetime.now().timestamp())}",
        "generated_at": now,
        "overall_readiness_score": 88,
        "target_role": target_role,
        "resume_intelligence": r_out["output"],
        "ats_optimization": a_out["output"],
        "job_intelligence": j_out["output"],
        "company_intelligence": c_out["output"],
        "skill_gap_analysis": s_out["output"],
        "career_roadmap": rm_out["output"],
        "market_trends": m_out["output"],
        "portfolio_recommendations": p_out["output"]
    }

    reports_col = db.get_collection("reports")
    await reports_col.insert_one(report_doc)

    return report_doc
