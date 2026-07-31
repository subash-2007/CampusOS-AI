import logging
import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

from app.agents.base_agent import BaseAgent
from app.agents.shared_memory import SharedMemory

logger = logging.getLogger("CampusOS.CareerOrchestrator")

class CareerOrchestratorAgent(BaseAgent):
    """Orchestrator Agent managing 28 specialized AI agents via Cloud LLMs (Anthropic Claude, Gemini, OpenAI, Tavily) with parallel execution and real-time MongoDB status updates."""
    def __init__(self):
        super().__init__(
            agent_id="career_orchestrator",
            name="Career Orchestrator Agent",
            description="Master agent orchestrating model routing, async parallel execution for all 28 AI agents, live session tracking, and error handling.",
            icon="Brain"
        )

    async def _run_agent_task(
        self,
        task_tuple: tuple,
        memory: SharedMemory,
        completed_agents: List[str],
        agent_outputs: Dict[str, Any],
        total_tasks_count: int,
        session_id: Optional[str] = None,
        mongo: Optional[Any] = None
    ) -> Optional[Dict[str, Any]]:
        """Executes a single agent task safely with error boundaries and MongoDB state updates."""
        from app.agents.registry import agent_registry

        agent_display_name, agent_id, inputs = task_tuple
        sub_agent = agent_registry.get_agent(agent_id)
        if not sub_agent:
            return None

        sessions_col = mongo.get_collection("analysis_sessions") if mongo else None
        outputs_col = mongo.get_collection("agent_outputs") if mongo else None

        try:
            memory.log_step(self.agent_id, f"Executing Cloud Agent: {agent_display_name}")
            res = await sub_agent.run(inputs, memory=memory)
            
            completed_agents.append(agent_display_name)
            agent_outputs[agent_id] = res

            # Save individual output in MongoDB `agent_outputs` collection
            if outputs_col and session_id:
                try:
                    await outputs_col.insert_one({
                        "session_id": session_id,
                        "agent_id": agent_id,
                        "agent_name": agent_display_name,
                        "response": res,
                        "created_at": datetime.now(timezone.utc).isoformat(),
                        "timestamp": datetime.now(timezone.utc).isoformat()
                    })
                except Exception as e:
                    logger.debug(f"Failed to persist output for {agent_id}: {e}")

            # Update live session progress in MongoDB `analysis_sessions`
            if sessions_col and session_id:
                progress_pct = int((len(completed_agents) / total_tasks_count) * 100)
                try:
                    await sessions_col.update_one(
                        {"_id": session_id},
                        {
                            "$addToSet": {"completed_agents": agent_display_name},
                            "$set": {
                                "active_agent": agent_display_name,
                                "progress_pct": progress_pct,
                                "status": "completed" if progress_pct >= 100 else "processing",
                                "updated_at": datetime.now(timezone.utc).isoformat()
                            }
                        }
                    )
                except Exception as e:
                    logger.debug(f"Failed updating session status: {e}")

            return res
        except Exception as err:
            logger.error(f"[{agent_id}] Parallel execution error: {err}")
            memory.log_step(self.agent_id, f"Error in {agent_display_name}: {err}")
            return None

    async def execute_all_agents(
        self,
        tasks: List[tuple],
        memory: SharedMemory,
        session_id: Optional[str] = None,
        mongo: Optional[Any] = None
    ) -> Dict[str, Any]:
        """Executes all 28 agents asynchronously in parallel batches using asyncio.gather to avoid timeouts."""
        completed_agents: List[str] = []
        agent_outputs: Dict[str, Any] = {}
        total_count = len(tasks)

        # Separate into 2 parallel batches for clean dependency execution
        batch_1_tasks = tasks[:20]  # Independent extraction/analysis agents
        batch_2_tasks = tasks[20:]  # Derived synthesis/coaching agents

        logger.info(f"Launching Batch 1 ({len(batch_1_tasks)} independent Cloud AI Agents in parallel)...")
        await asyncio.gather(*[
            self._run_agent_task(t, memory, completed_agents, agent_outputs, total_count, session_id, mongo)
            for t in batch_1_tasks
        ], return_exceptions=True)

        logger.info(f"Launching Batch 2 ({len(batch_2_tasks)} synthesis/coaching Cloud AI Agents in parallel)...")
        await asyncio.gather(*[
            self._run_agent_task(t, memory, completed_agents, agent_outputs, total_count, session_id, mongo)
            for t in batch_2_tasks
        ], return_exceptions=True)

        return agent_outputs

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        prompt = inputs.get("prompt", "")
        context = inputs.get("context", {})
        
        dynamic_data = {
            "response": f"I am your CampusOS Career Orchestrator. Regarding '{prompt if prompt else 'your career journey'}': I recommend analyzing your resume with our **Resume Intelligence Agent** and benchmarking against your target job role using our **28 Specialized Cloud AI Agents**.",
            "suggested_agents": ["resume_intelligence", "ats_optimization", "interview_intelligence"],
            "recommended_actions": [
                "Upload your latest PDF/DOCX resume",
                "Paste target Job Description to benchmark your match score",
                "Review customized 30-60-90 day career roadmap"
            ],
            "confidence_score": 98
        }

        system_prompt = (
            "You are the Master Career Orchestrator Agent for CampusOS AI. Provide structured, clear, highly encouraging, "
            "and actionable response in JSON format with keys: 'response', 'suggested_agents', 'recommended_actions', 'confidence_score'."
        )

        user_prompt = f"User Request: {prompt}\nContext: {context}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "output": output
        }
