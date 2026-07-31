import logging
from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.agents.shared_memory import SharedMemory

logger = logging.getLogger("CampusOS.AdvancedAgents")

# 15. Learning Resource Agent
class LearningResourceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="learning_resource",
            name="Learning Resource Agent",
            description="Recommends curated courses, technical documentation, and practice labs for targeted skill gaps.",
            icon="BookOpen"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")
        missing_skills = (memory.skill_gap_analysis.get("missing_skills") if memory and memory.skill_gap_analysis else None) or ["System Design", "Cloud Infrastructure"]

        fallback = {
            "score": 90,
            "courses": [f"Mastering {sk} for {target_role}" for sk in missing_skills[:2]] + ["Production System Architecture & Microservices"],
            "documentation": [f"Official {sk} Documentation & Guides" for sk in missing_skills[:2]],
            "practice_labs": ["LeetCode / HackerRank DSA Practice", "GitHub Hands-On Microservices Lab"],
            "recommended_platforms": ["Coursera", "Udemy", "LeetCode", "ByteByteGo"]
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Learning Architect & Technical Curriculum Developer",
            domain_focus="Curating high-impact technical courses, official documentation pathways, and production practice labs for skill gap remediation."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="learning_resource", preferred_engine="gemini")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.learning_resources = res
        return res


# 16. Certification Advisor Agent
class CertificationAdvisorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="certification_advisor",
            name="Certification Advisor Agent",
            description="Provides a strategic certification roadmap aligned with target industry benchmarks.",
            icon="Award"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 88,
            "recommended_certifications": [
                f"AWS Certified Solutions Architect / Cloud Practitioner ({target_role})",
                "Certified Kubernetes Application Developer (CKAD)",
                "Meta Front-End / Back-End Developer Professional Certificate"
            ],
            "certification_roadmap": "Obtain Cloud certification within 60 days to boost ATS resume parsing weights by 25%.",
            "priority": "High"
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Certification Consultant & Credential Strategist",
            domain_focus="Industry credential benchmarking, cloud certification roadmapping, and resume verification weighting."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="certification_advisor", preferred_engine="gemini")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.certification_plan = res
        return res


# 17. Coding Assessment Agent
class CodingAssessmentAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="coding_assessment",
            name="Coding Assessment Agent",
            description="Generates role-specific coding problems, DSA evaluations, and solution breakdowns.",
            icon="Code"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 85,
            "assessment_title": f"Production Data Pipeline & Algorithmic Challenge for {target_role}",
            "dsa_focus": ["Hash Maps & Graphs", "LRU Cache / Concurrent Queues", "Time/Space Complexity O(N)"],
            "sample_problem": "Design an in-memory rate-limiter supporting sliding window algorithm with O(1) time complexity.",
            "evaluation_criteria": ["Correctness & Edge Cases", "Clean Code & Modularity", "Optimal Time Complexity"]
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Senior Coding Evaluator & Principal Technical Examiner",
            domain_focus="Role-specific coding challenges, data structure algorithms, time/space complexity trade-off evaluation, and clean code scoring."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="coding_assessment", preferred_engine="gemini")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.coding_assessment = res
        return res


# 18. Recruiter Simulation Agent
class RecruiterSimulationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="recruiter_simulation",
            name="Recruiter Simulation Agent",
            description="Simulates top tech recruiter screening evaluations and flags 6-second resume rejection risks.",
            icon="UserCheck"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 84,
            "first_impression_score": 84,
            "recruiter_verdict": f"Strong potential for {target_role}, but bullet points need quantifiable business metrics.",
            "rejection_risks": [
                "Lack of explicit metrics (e.g., % performance boost or user growth)",
                "Missing keywords for primary target tech stack in summary section",
                "Project descriptions focus on tools rather than outcomes"
            ],
            "action_advice": "Convert passive bullet points into action verb + metric structures."
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Senior Talent Acquisition Manager",
            domain_focus="Simulating 6-second initial recruiter resume screens, identifying pass/fail rejection risks, and visual scan optimization."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="recruiter_simulation", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.recruiter_feedback = res
        return res


# 19. Behavioral Intelligence Agent
class BehavioralIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="behavioral_intelligence",
            name="Behavioral Intelligence Agent",
            description="Analyzes communication impact, leadership signals, and confidence tone in candidate responses.",
            icon="Smile"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 86,
            "confidence_score": 86,
            "leadership_signals": ["Cross-functional teamwork", "Ownership during outages/bugs", "Mentoring junior peers"],
            "star_completeness": "Good situation/task context; ensure Action and Result sections contain numeric outcomes.",
            "behavioral_tips": ["Use 'I led' and 'I built' instead of passive 'We did'", "Keep answers under 2 minutes"]
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Organizational Psychologist & Executive Behavioral Assessor",
            domain_focus="Behavioral interview response evaluation, leadership signal extraction, STAR framework completeness, and confidence tone analysis."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="behavioral_intelligence", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.behavioral_analysis = res
        return res


# 20. Career Risk Assessment Agent
class CareerRiskAssessmentAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="career_risk_assessment",
            name="Career Risk Assessment Agent",
            description="Identifies potential career stagnation threats, market automation risks, and skill obsolescence.",
            icon="AlertTriangle"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 88,
            "risk_level": "Low - High Growth Demand Area",
            "threat_factors": [
                "Over-reliance on legacy frameworks without cloud-native experience",
                "Automated AI coding tools displacing entry-level boilerplate development"
            ],
            "mitigation_strategy": f"Gain hands-on proficiency in AI agent engineering, cloud architecture, and system design for {target_role}."
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Career Risk Consultant & Tech Disruption Analyst",
            domain_focus="Identifying tech skill obsolescence, AI automation threats, career stagnation risks, and mitigation strategies."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="career_risk_assessment", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.career_risk = res
        return res


# 21. AI Mentor Agent
class AIMentorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="ai_mentor",
            name="AI Mentor Agent",
            description="Provides daily actionable career coaching, motivational guidance, and mindset routines.",
            icon="Compass"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")
        career_goal = inputs.get("career_goal") or (memory.career_goal if memory else f"Land a role as {target_role}")

        fallback = {
            "score": 92,
            "daily_mantra": f"Focus on building 1 production feature every day to stand out as a top candidate for {target_role}.",
            "weekly_action_items": [
                "Solve 5 Medium DSA questions focusing on target interview patterns.",
                "Deploy a live web project demo with public GitHub documentation.",
                "Send 3 tailored outreach notes to engineering managers."
            ],
            "mentorship_note": "Consistency compounds. Small daily iterations lead to placement success."
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Personal Career Mentor & Executive Performance Coach",
            domain_focus="Daily career mindset coaching, weekly goal setting, professional accountability, and career momentum routines."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="ai_mentor", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.ai_mentor = res
        return res


# 22. Professional Branding Agent
class ProfessionalBrandingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="professional_branding",
            name="Professional Branding Agent",
            description="Optimizes LinkedIn profile headline/about section and GitHub repository presentation.",
            icon="Share2"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 88,
            "linkedin_headline": f"{target_role} | Building Scalable Full-Stack Systems & AI Applications | Tech Explorer",
            "linkedin_about_snippet": f"Passionate {target_role} specialized in building high-performance web applications, distributed APIs, and AI integrations. Open to software engineering roles.",
            "github_branding_tips": [
                "Add a sleek GitHub Profile README with tech stack badges and dynamic stats.",
                "Ensure top 3 pinned repositories have live demo links, screenshots, and architecture diagrams."
            ]
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Personal Branding Consultant & Technical Copywriter",
            domain_focus="LinkedIn profile optimization, GitHub bio branding, personal brand positioning, and recruiter attraction copywriting."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="professional_branding", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.professional_branding = res
        return res


# 23. Project Innovation Agent
class ProjectInnovationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="project_innovation",
            name="Project Innovation Agent",
            description="Suggests innovative portfolio project ideas and enterprise-grade architecture upgrades.",
            icon="Lightbulb"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 90,
            "recommended_projects": [
                {
                    "title": f"Autonomous Multi-Agent AI System for {target_role}",
                    "tech_stack": "Next.js 15, FastAPI, MongoDB, Anthropic Claude / Gemini",
                    "key_feature": "Real-time task orchestration with WebSocket progress streaming."
                },
                {
                    "title": "High-Throughput Microservice Analytics Platform",
                    "tech_stack": "Go / Python FastAPI, Redis, PostgreSQL, Docker",
                    "key_feature": "Distributed rate limiting and telemetry tracking."
                }
            ]
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Innovation Architect & Tech Stack Visionary",
            domain_focus="Designing flagship portfolio projects, recommending enterprise tech stacks, and integrating cutting-edge AI architecture."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="project_innovation", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.project_innovation = res
        return res


# 24. Technical Architecture Review Agent
class TechnicalArchitectureReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="technical_architecture_review",
            name="Technical Architecture Review Agent",
            description="Evaluates candidate project architectures for security, scalability, and design patterns.",
            icon="Layers"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 88,
            "architecture_score": 88,
            "security_assessment": "JWT Bearer Authentication implemented; add rate-limiting headers and input sanitization.",
            "scalability_rating": "High - Async FastAPI + MongoDB allows horizontal scaling for read/write workloads.",
            "recommended_upgrades": [
                "Implement Redis caching for frequent database queries",
                "Containerize app with Docker Compose for repeatable deployments"
            ]
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Principal Software Architect",
            domain_focus="System architecture review, microservices design pattern audit, database scalability analysis, and security hardening."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="technical_architecture_review", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.architecture_review = res
        return res


# 25. AI Hiring Manager Agent
class AIHiringManagerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="ai_hiring_manager",
            name="AI Hiring Manager Agent",
            description="Simulates final Engineering Director hire/reject decisions with detailed trade-off reasoning.",
            icon="CheckSquare"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 90,
            "hiring_decision": "HIRE / RECOMMEND FOR ONSITE INTERVIEW",
            "decision_confidence": "88% Match Confidence",
            "key_positives": [
                f"Candidate technical foundation matches core requirements for {target_role}",
                "Demonstrates proactive project building and modern stack experience"
            ],
            "areas_to_verify_in_onsite": [
                "Depth of system design edge-case handling",
                "Hands-on debugging speed under pressure"
            ]
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Engineering Director & Final Hiring Decision Bar Raiser",
            domain_focus="Final candidate hiring decisions, trade-off evaluation, engineering team fit assessment, and onsite verification topics."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="ai_hiring_manager", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.hiring_manager_decision = res
        return res


# 26. Industry Benchmark Agent
class IndustryBenchmarkAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="industry_benchmark",
            name="Industry Benchmark Agent",
            description="Benchmarks candidate profile against top percentile applicants in tech hubs.",
            icon="Sliders"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 85,
            "percentile_rank": "Top 15th Percentile Applicant",
            "peer_comparison": f"Stronger technical project portfolio than 85% of applicants competing for {target_role}.",
            "differentiating_factors": ["Multi-agent system experience", "Full-stack integration speed"]
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Industry Benchmark Analyst & Talent Intelligence Specialist",
            domain_focus="Benchmarking candidate competitiveness against top 10% tech talent pools, percentile ranking, and differentiator identification."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="industry_benchmark", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.industry_benchmark = res
        return res


# 27. Offer Evaluation Agent
class OfferEvaluationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="offer_evaluation",
            name="Offer Evaluation Agent",
            description="Analyzes salary benchmarks, total compensation equity, and negotiation strategies.",
            icon="DollarSign"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")
        company_name = inputs.get("company_name") or (memory.company_name if memory else "Target Enterprise")

        fallback = {
            "score": 90,
            "estimated_base_salary_range": "$85,000 - $125,000 USD (depending on tier & region)",
            "compensation_equity_note": "Target signing bonus or equity grant between 10-15% of annual base.",
            "negotiation_script": f"Thank you for the offer for {target_role} at {company_name}. Based on my technical background and competing market offers, I would like to discuss adjusting the base salary to..."
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Compensation & HR Consultant",
            domain_focus="Salary package evaluation, equity equity breakdown, counteroffer negotiation scripting, and total compensation optimization."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="offer_evaluation", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.offer_evaluation = res
        return res


# 28. Career Success Prediction Agent
class CareerSuccessPredictionAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="career_success_prediction",
            name="Career Success Prediction Agent",
            description="Predicts 1-year and 3-year career growth velocity and offer placement probability.",
            icon="TrendingUp"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[SharedMemory] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        fallback = {
            "score": 89,
            "placement_probability_30_days": "78% Probability of Initial Screening / Phone Technicals",
            "placement_probability_60_days": "89% Probability of Final Round / Offer Placement",
            "year_1_trajectory": f"Senior {target_role} track within 14-18 months based on continuous skill building.",
            "career_growth_velocity": "High / Accelerated Growth Trajectory"
        }

        system_prompt = self.build_expert_system_prompt(
            persona_role="Career Strategy Advisor & Predictive Growth Analyst",
            domain_focus="1-year and 3-year career trajectory forecasting, placement timeline prediction, and leadership promotion velocity."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        raw_resp = await self.call_llm(system_prompt, user_prompt, task_type="career_success_prediction", preferred_engine="anthropic")
        res = self.parse_agent_output(raw_resp, fallback)

        if memory:
            memory.career_prediction = res
        return res
