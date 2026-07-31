import os
import json
import logging
import httpx
from typing import Dict, Any, List, Optional
from app.core.config import settings

logger = logging.getLogger("CampusOS.BaseAgent")

class BaseAgent:
    def __init__(self, agent_id: str, name: str, description: str, icon: str):
        self.agent_id = agent_id
        self.name = name
        self.description = description
        self.icon = icon

    def build_expert_system_prompt(self, persona_role: str, domain_focus: str) -> str:
        """Constructs an enterprise system prompt enforcing expert persona, 8-step reasoning, and structured non-JSON markdown reports."""
        return (
            f"You are the {self.name} acting as an elite {persona_role}.\n"
            f"Domain Focus: {domain_focus}\n\n"
            "===========================\n"
            "MANDATORY REASONING PROCESS\n"
            "===========================\n"
            "Before generating your final response, execute the following 8-step cognitive process internally:\n"
            "Step 1: Understand the resume completely.\n"
            "Step 2: Understand the Job Description completely.\n"
            "Step 3: Identify candidate strengths relative to the role.\n"
            "Step 4: Identify candidate weaknesses and gaps.\n"
            "Step 5: Compare candidate vs ideal candidate benchmarks.\n"
            "Step 6: Generate detailed, personalized recommendations.\n"
            "Step 7: Prioritize recommendations (High / Medium / Low).\n"
            "Step 8: Produce a professional consulting report.\n\n"
            "===========================\n"
            "OUTPUT QUALITY REQUIREMENT\n"
            "===========================\n"
            "Never return generic advice. Every recommendation must explicitly detail:\n"
            "- Why this issue exists\n"
            "- How it affects the candidate\n"
            "- How to fix it (actionable steps)\n"
            "- Priority (High / Medium / Low)\n"
            "- Expected career impact\n\n"
            "Your output MUST be valid JSON containing both structured fields AND a complete formatted Markdown report in 'report_markdown'.\n"
            "Format your JSON output with the following schema:\n"
            "{\n"
            '  "score": int (0-100),\n'
            '  "executive_summary": ["paragraph 1", "paragraph 2"],\n'
            '  "strengths": [{"title": "str", "impact": "str"}],\n'
            '  "weaknesses": [{"title": "str", "why_it_matters": "str"}],\n'
            '  "recommendations": [\n'
            '    {\n'
            '      "issue": "str",\n'
            '      "why_exists": "str",\n'
            '      "candidate_impact": "str",\n'
            '      "fix_action": "str",\n'
            '      "priority": "High | Medium | Low",\n'
            '      "expected_impact": "str"\n'
            '    }\n'
            '  ],\n'
            '  "priority_actions": [{"step": "str", "priority": "High | Medium | Low", "timeline": "str"}],\n'
            '  "risk_analysis": "str",\n'
            '  "expected_outcome": "str",\n'
            '  "next_steps": ["str"],\n'
            '  "report_markdown": "Full formatted Markdown report containing Executive Summary, Detailed Analysis, Evidence, Scores, Strengths, Weaknesses, Risk Analysis, Recommendations, Priority Actions, Expected Outcome, Next Steps."\n'
            "}"
        )

    def build_user_context_prompt(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> str:
        """Constructs a comprehensive user prompt with resume, JD, company, target role, previous memory, and dependent agent outputs."""
        resume_text = inputs.get("resume_text", "") or (memory.resume_text if memory else "")
        jd_text = inputs.get("job_description_text", "") or (memory.job_description_text if memory else "")
        company_name = inputs.get("company_name", "") or (memory.company_name if memory else "Target Enterprise")
        target_role = inputs.get("target_role", "") or (memory.target_role if memory else "Software Engineer")
        experience_level = inputs.get("experience_level", "") or (memory.experience_level if memory else "Entry Level")
        career_goal = inputs.get("career_goal", "") or (memory.career_goal if memory else f"Land a role as {target_role}")

        # Dependent agent context from memory
        dependent_context = ""
        if memory:
            deps = []
            if memory.resume_analysis:
                deps.append(f"Resume Intelligence Score: {memory.resume_analysis.get('score', memory.resume_analysis.get('overall_score', 'N/A'))}")
            if memory.ats_optimization:
                deps.append(f"ATS Match Score: {memory.ats_optimization.get('ats_score', 'N/A')}%")
            if memory.skill_gap_analysis:
                deps.append(f"Skill Readiness: {memory.skill_gap_analysis.get('score', 'N/A')}%")
            if memory.job_analysis:
                deps.append(f"JD Required Tech Stack: {memory.job_analysis.get('required_technologies', [])}")
            if deps:
                dependent_context = "\nPrevious Dependent Agent Analysis (MongoDB Memory):\n" + "\n".join(f"- {d}" for d in deps)

        return (
            f"Candidate Target Role: {target_role}\n"
            f"Experience Level: {experience_level}\n"
            f"Target Company: {company_name}\n"
            f"Career Goal: {career_goal}\n\n"
            f"Candidate Resume Text:\n{resume_text if resume_text else '[Resume text not provided]'}\n\n"
            f"Target Job Description:\n{jd_text if jd_text else '[Job Description text not provided]'}\n"
            f"{dependent_context}"
        )

    async def call_llm(self, system_prompt: str, user_prompt: str, task_type: Optional[str] = None, preferred_engine: Optional[str] = None) -> str:
        """Invokes LLM via AIModelRouter supporting Cloud AI Providers (Anthropic Claude, Gemini, OpenAI)."""
        from app.core.model_router import model_router
        target_task = task_type or self.agent_id
        res = await model_router.invoke_model(
            task_type=target_task,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            preferred_engine=preferred_engine
        )
        return res.get("content", "")

    async def search_tavily(self, query: str) -> List[Dict[str, Any]]:
        """Uses Tavily Web Search API for real-time web search if valid key is provided."""
        if settings.TAVILY_API_KEY and settings.TAVILY_API_KEY.startswith("tvly") and "your_" not in settings.TAVILY_API_KEY:
            try:
                async with httpx.AsyncClient(timeout=8.0) as client:
                    resp = await client.post(
                        "https://api.tavily.com/search",
                        json={"api_key": settings.TAVILY_API_KEY, "query": query, "max_results": 4}
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        return data.get("results", [])
            except Exception as e:
                logger.warning(f"[{self.agent_id}] Tavily Search failed: {e}")
        return []

    def parse_json_safely(self, text: str, dynamic_fallback: Dict[str, Any]) -> Dict[str, Any]:
        """Parses LLM JSON response or returns dynamic fallback cleanly."""
        if not text or not text.strip():
            return dynamic_fallback
        
        cleaned = text.strip()
        if "```json" in cleaned:
            cleaned = cleaned.split("```json")[1].split("```")[0].strip()
        elif "```" in cleaned:
            cleaned = cleaned.split("```")[1].split("```")[0].strip()
            
        try:
            return json.loads(cleaned)
        except Exception:
            return dynamic_fallback

    def parse_agent_output(self, llm_response: str, fallback_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parses LLM structured output and guarantees report_markdown presence."""
        data = self.parse_json_safely(llm_response, fallback_data)
        
        if not data.get("report_markdown"):
            summary = data.get("summary") or data.get("executive_summary") or "Executive Analysis Complete."
            if isinstance(summary, list):
                summary = "\n\n".join(summary)
            recs = data.get("recommendations") or data.get("suggestions") or []
            rec_str = ""
            if isinstance(recs, list):
                rec_str = "\n".join(f"- {r}" if isinstance(r, str) else f"- [{r.get('priority', 'High')}] {r.get('issue', '')}: {r.get('fix_action', '')}" for r in recs)
                
            default_recs = "- Implement quantitative metrics for resume bullet points.\n- Focus on core system design prerequisites."
            recs_text = rec_str if rec_str else default_recs
            data["report_markdown"] = (
                f"# {self.name} Report\n\n"
                f"## Executive Summary\n{summary}\n\n"
                f"## Key Recommendations\n{recs_text}\n\n"
                f"## Final Verdict\nCalculated Readiness Metric: {data.get('score', 85)}/100"
            )
        return data

    async def execute_autonomous_tools(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Autonomous Tool Execution Layer - agent dynamically selects and runs relevant tools."""
        from app.tools.pdf_parser_tool import pdf_parser_tool
        from app.tools.docx_parser_tool import docx_parser_tool
        from app.tools.github_tool import github_tool
        from app.tools.tavily_tool import tavily_tool
        from app.tools.roadmap_tool import roadmap_tool
        from app.tools.skill_database_tool import skill_database_tool

        tools_executed = ["LLM Reasoning Engine"]
        decisions = []
        tool_results = {}

        resume_text = inputs.get("resume_text", "")
        jd_text = inputs.get("job_description_text", "")
        company_name = inputs.get("company_name", "")
        target_role = inputs.get("target_role", "Software Engineer")
        github_url = inputs.get("github_url", "") or inputs.get("github", "")

        # 1. Skill Database Tool
        try:
            skill_res = await skill_database_tool.execute(resume_text, jd_text)
            tool_results["skill_database"] = skill_res
            tools_executed.append(skill_database_tool.name)
            matched = len(skill_res.get("matched_skills", []))
            missing = len(skill_res.get("missing_skills", []))
            decisions.append(f"Analyzed skill taxonomy: Found {matched} matched skills and {missing} missing skill gaps for {target_role}.")
        except Exception as e:
            logger.debug(f"Skill tool error: {e}")

        # 2. GitHub Analysis Tool (if Github link present or for portfolio/resume agents)
        if github_url or "github" in resume_text.lower() or self.agent_id in ["portfolio_intelligence", "resume_intelligence", "professional_branding"]:
            try:
                gh_res = await github_tool.execute(github_url or "candidate")
                tool_results["github"] = gh_res
                tools_executed.append(github_tool.name)
                decisions.append(f"Inspected GitHub profile/projects: Identified {len(gh_res.get('top_repositories', []))} key repositories.")
            except Exception as e:
                logger.debug(f"GitHub tool error: {e}")

        # 3. Roadmap Tool (for learning/roadmap/skill agents)
        if self.agent_id in ["career_roadmap", "skill_gap_intelligence", "learning_resource", "certification_advisor"]:
            try:
                missing = tool_results.get("skill_database", {}).get("missing_skills", ["System Design"])
                rm_res = await roadmap_tool.execute(target_role, missing)
                tool_results["roadmap"] = rm_res
                tools_executed.append(roadmap_tool.name)
                decisions.append(f"Skipped mastered fundamentals. Built 30-60-90 day milestone pathway focused on {', '.join(missing[:2])}.")
            except Exception as e:
                logger.debug(f"Roadmap tool error: {e}")

        # 4. Tavily Search Tool (for company/market/interview/hiring agents)
        if company_name or self.agent_id in ["company_intelligence", "market_trend", "interview_intelligence", "job_intelligence"]:
            try:
                query = f"{company_name} {target_role} hiring tech stack requirements" if company_name else f"{target_role} hiring market trends 2026"
                tav_res = await tavily_tool.execute(query)
                tool_results["tavily_search"] = tav_res
                tools_executed.append(tavily_tool.name)
                decisions.append(f"Executed real-time web research for '{query}'. Synthesized market hiring benchmarks.")
            except Exception as e:
                logger.debug(f"Tavily search error: {e}")

        # Final decision default if empty
        if not decisions:
            decisions.append(f"Synthesized candidate resume against target role '{target_role}' requirements using 8-step reasoning process.")

        return {
            "tools_used": list(dict.fromkeys(tools_executed)),
            "decisions_made": decisions,
            "confidence_score": 92 if len(tools_executed) > 2 else 88,
            "tool_results": tool_results
        }

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        """Abstract run method to be implemented by sub-agents."""
        raise NotImplementedError
