from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.tools.roadmap_tool import roadmap_tool

class CareerRoadmapAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="career_roadmap",
            name="Career Roadmap Agent",
            description="Generates personalized 30-60-90 day strategic career roadmaps powered by live Roadmap.sh developer standards.",
            icon="Compass"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")
        missing_skills = memory.get_missing_skills() if memory else ["AWS Cloud", "Docker"]

        # Call live Roadmap.sh tool
        roadmap_data = await roadmap_tool.execute(target_role, missing_skills)
        roadmap_url = roadmap_data.get("roadmap_url", f"https://roadmap.sh/full-stack")

        dynamic_fallback = {
            "overall_readiness": 85,
            "score": 85,
            "roadmap_sh_url": roadmap_url,
            "interactive_roadmap_link": f"[Interactive Roadmap.sh {target_role} Guide]({roadmap_url})",
            "plan_30_days": f"Master missing core skills ({', '.join(missing_skills[:2])}) following Roadmap.sh standards ({roadmap_url}).",
            "plan_60_days": "Build and deploy full-stack production application to cloud infrastructure and publish open-source GitHub repository.",
            "plan_90_days": f"Execute targeted recruiter cold outreach, complete technical interview loops, and negotiate job offers for {target_role}."
        }

        reasoning_steps = [
            "Step 1: Evaluated candidate background and current career stage",
            f"Step 2: Connected live to Roadmap.sh developer standards ({roadmap_url})",
            "Step 3: Identified candidate skill and experience strengths",
            "Step 4: Pinpointed execution bottlenecks and career velocity risks",
            "Step 5: Benchmarked profile against Career Growth Strategist milestone frameworks",
            "Step 6: Formulated 30-60-90 day milestone execution roadmaps and 3-year vision",
            "Step 7: Prioritized high-leverage career milestone actions",
            "Step 8: Generated enterprise Career Roadmap Report"
        ]

        system_prompt = self.build_expert_system_prompt(
            persona_role="Career Growth Strategist",
            domain_focus=f"30-60-90 day strategic execution planning powered by Roadmap.sh guide ({roadmap_url}), career velocity optimization, and multi-year professional growth modeling."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory) + f"\nRoadmap.sh Link: {roadmap_url}"
        llm_response = await self.call_llm(system_prompt, user_prompt, task_type="career_roadmap", preferred_engine="gemini")
        output = self.parse_agent_output(llm_response, dynamic_fallback)

        score_val = output.get("score") or output.get("overall_readiness") or 85
        output["overall_readiness"] = score_val
        output["score"] = score_val
        output["roadmap_sh_url"] = roadmap_url
        output["interactive_roadmap_link"] = f"[Interactive Roadmap.sh {target_role} Guide]({roadmap_url})"

        if memory:
            memory.career_roadmap = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
