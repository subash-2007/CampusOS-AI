import logging
from typing import Dict, List, Any
from app.agents.base_agent import BaseAgent
from app.agents.orchestrator_agent import CareerOrchestratorAgent
from app.agents.resume_intelligence_agent import ResumeIntelligenceAgent
from app.agents.ats_optimization_agent import ATSOptimizationAgent
from app.agents.job_intelligence_agent import JobIntelligenceAgent
from app.agents.company_intelligence_agent import CompanyIntelligenceAgent
from app.agents.skill_gap_agent import SkillGapAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.career_roadmap_agent import CareerRoadmapAgent
from app.agents.career_analytics_agent import CareerAnalyticsAgent
from app.agents.memory_agent import MemoryAgent
from app.agents.market_trend_agent import MarketTrendAgent
from app.agents.document_verification_agent import DocumentVerificationAgent
from app.agents.portfolio_agent import PortfolioAgent
from app.agents.communication_agent import CommunicationAgent

logger = logging.getLogger("CampusOS.AgentRegistry")

class AgentRegistry:
    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {
            "career_orchestrator": CareerOrchestratorAgent(),
            "resume_intelligence": ResumeIntelligenceAgent(),
            "ats_optimization": ATSOptimizationAgent(),
            "job_intelligence": JobIntelligenceAgent(),
            "company_intelligence": CompanyIntelligenceAgent(),
            "skill_gap_intelligence": SkillGapAgent(),
            "interview_intelligence": InterviewAgent(),
            "career_roadmap": CareerRoadmapAgent(),
            "career_analytics": CareerAnalyticsAgent(),
            "memory_personalization": MemoryAgent(),
            "market_trend": MarketTrendAgent(),
            "document_verification": DocumentVerificationAgent(),
            "portfolio_intelligence": PortfolioAgent(),
            "communication_intelligence": CommunicationAgent()
        }

    def get_agent(self, agent_id: str) -> BaseAgent:
        return self.agents.get(agent_id, self.agents["career_orchestrator"])

    def list_agents(self) -> List[Dict[str, str]]:
        return [
            {
                "id": agent.agent_id,
                "name": agent.name,
                "description": agent.description,
                "icon": agent.icon
            }
            for agent in self.agents.values()
        ]

agent_registry = AgentRegistry()
