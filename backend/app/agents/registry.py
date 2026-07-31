import os
import logging
import importlib
from typing import Dict, List, Any
from app.agents.base_agent import BaseAgent
from app.agents.orchestrator_agent import CareerOrchestratorAgent

logger = logging.getLogger("CampusOS.AgentRegistry")

class AgentRegistry:
    """Registry maintaining all 111 Departments and 1,111 specialized AI Agents."""
    def __init__(self):
        self.agents: Dict[str, Any] = {
            "career_orchestrator": CareerOrchestratorAgent(),
        }
        self.departments: List[Dict[str, Any]] = []
        self._load_all_departments()

    def _load_all_departments(self):
        dept_base = r"d:\CampusOS\departments"
        if not os.path.exists(dept_base):
            return

        dept_dirs = sorted([
            d for d in os.listdir(dept_base)
            if os.path.isdir(os.path.join(dept_base, d)) and d != "shared"
        ])

        for idx, dname in enumerate(dept_dirs, 1):
            did = f"dept_{idx:03d}"
            formatted_name = dname.replace("_", " ").title()
            
            dept_obj = {
                "id": did,
                "dirname": dname,
                "name": formatted_name,
                "agents_count": 10,
                "agents": []
            }

            try:
                det_mod = importlib.import_module(f"departments.{dname}.deterministic")
                reas_mod = importlib.import_module(f"departments.{dname}.reasoning")
                orch_mod = importlib.import_module(f"departments.{dname}.orchestrator")

                # Load Orchestrator
                for attr in dir(orch_mod):
                    if attr.endswith("OrchestratorAgent"):
                        cls = getattr(orch_mod, attr)
                        inst = cls()
                        self.agents[dname] = inst
                        self.agents[did] = inst
                        dept_obj["agents"].append({
                            "id": inst.agent_id,
                            "name": inst.name,
                            "type": "Orchestrator",
                            "description": getattr(inst, "description", f"Master Orchestrator for {formatted_name}"),
                            "icon": getattr(inst, "icon", "Cpu")
                        })
                        break

                # Load Reasoning Agents
                for attr in dir(reas_mod):
                    if attr.endswith("Agent"):
                        cls = getattr(reas_mod, attr)
                        try:
                            inst = cls()
                            agent_id = getattr(inst, "agent_id", f"{dname}_{attr.lower()}")
                            self.agents[agent_id] = inst
                            dept_obj["agents"].append({
                                "id": agent_id,
                                "name": getattr(inst, "name", attr),
                                "type": "Reasoning",
                                "description": getattr(inst, "description", f"Reasoning agent for {formatted_name}"),
                                "icon": getattr(inst, "icon", "Brain")
                            })
                        except Exception:
                            pass

                # Load Deterministic Agents
                for attr in dir(det_mod):
                    if attr.endswith("Agent"):
                        cls = getattr(det_mod, attr)
                        try:
                            inst = cls()
                            agent_id = f"{dname}_{attr.lower()}"
                            self.agents[agent_id] = inst
                            dept_obj["agents"].append({
                                "id": agent_id,
                                "name": attr,
                                "type": "Deterministic",
                                "description": getattr(cls, "__doc__", f"Deterministic agent for {formatted_name}").strip(),
                                "icon": "CheckCircle"
                            })
                        except Exception:
                            pass

            except Exception as e:
                logger.warning(f"Could not dynamically register department {dname}: {e}")

            self.departments.append(dept_obj)

    def get_agent(self, agent_id: str) -> BaseAgent:
        clean_id = agent_id.replace("-", "_")
        if clean_id in self.agents:
            return self.agents[clean_id]
        return self.agents.get(agent_id, self.agents["career_orchestrator"])

    def list_departments(self) -> List[Dict[str, Any]]:
        return self.departments

    def list_agents(self) -> List[Dict[str, Any]]:
        all_agents = []
        seen = set()
        for dept in self.departments:
            for ag in dept["agents"]:
                if ag["id"] not in seen:
                    seen.add(ag["id"])
                    all_agents.append(ag)
        return all_agents

agent_registry = AgentRegistry()
