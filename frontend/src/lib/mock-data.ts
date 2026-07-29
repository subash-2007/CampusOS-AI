import { AgentMetadata, UserProfile, FullReport } from './types';

export const MOCK_USER: UserProfile = {
  id: "demo-user-123",
  email: "demo@campusos.ai",
  full_name: "Alex Mercer",
  target_role: "Full Stack Software Engineer",
  experience_level: "Entry Level / Student",
  created_at: "2026-01-15T08:00:00Z",
  updated_at: "2026-07-29T08:00:00Z"
};

export const MOCK_AGENTS: AgentMetadata[] = [
  { id: "career_orchestrator", name: "Career Orchestrator", description: "Master AI routing queries & coordinating agent workflows", icon: "Brain" },
  { id: "resume_intelligence", name: "Resume Intelligence", description: "Parses, analyzes formatting, structure, impact metrics & strengths", icon: "FileText" },
  { id: "ats_optimization", name: "ATS Optimization", description: "Calculates match %, keyword gaps, ATS compliance score & bullet rewriter", icon: "CheckCircle" },
  { id: "job_intelligence", name: "Job Intelligence", description: "Deconstructs Job Descriptions into core domain requirements & tech stacks", icon: "Briefcase" },
  { id: "company_intelligence", name: "Company Intelligence", description: "Researches company culture, interview focus & live web news via Tavily", icon: "Building" },
  { id: "skill_gap_intelligence", name: "Skill Gap Intelligence", description: "Identifies missing skills & creates prioritized learning pathways", icon: "Zap" },
  { id: "interview_intelligence", name: "Interview Intelligence", description: "Generates technical/behavioral Q&A, mock simulations & STAR reviews", icon: "MessageSquare" },
  { id: "career_roadmap", name: "Career Roadmap", description: "Generates 30-60-90 day milestone career plans & salary trajectories", icon: "Compass" },
  { id: "career_analytics", name: "Career Analytics", description: "Aggregates performance metrics, readiness score breakdown & market data", icon: "BarChart3" },
  { id: "memory_personalization", name: "Memory & Personalization", description: "Stores candidate preferences, skill history & context across sessions", icon: "Database" },
  { id: "market_trend", name: "Market Trend Intelligence", description: "Fetches live hiring trends, top requested skills & salary benchmarks", icon: "TrendingUp" },
  { id: "document_verification", name: "Document Verification", description: "Checks resume consistency, timeline validation & credential formats", icon: "ShieldCheck" },
  { id: "portfolio_intelligence", name: "Portfolio Intelligence", description: "Evaluates GitHub portfolio, project ideas & automated README builder", icon: "FolderGit2" },
  { id: "communication_intelligence", name: "Communication Intelligence", description: "Drafts cold emails, recruiter LinkedIn notes & salary negotiation scripts", icon: "Send" }
];

export const MOCK_ANALYTICS = {
  analytics: {
    readiness_score: 86,
    market_percentile: "Top 12% among Entry-Level Candidates",
    breakdown: {
      resume_quality: 85,
      ats_match: 82,
      technical_depth: 88,
      interview_readiness: 79,
      portfolio_impact: 91
    },
    skill_distribution: [
      { name: "Frontend (React/TS)", value: 35 },
      { name: "Backend (FastAPI/Python)", value: 30 },
      { name: "Database & Storage", value: 15 },
      { name: "DevOps & Tooling", value: 10 },
      { name: "System Architecture", value: 10 }
    ],
    key_insights: [
      "Your portfolio impact score (91%) is your strongest market differentiator",
      "Increasing interview mock practice sessions by 2 hours will push readiness score above 90%",
      "Top matched technical stacks: Next.js + FastAPI + MongoDB"
    ]
  },
  market_trends: {
    domain: "Full Stack Software Engineering",
    hiring_demand_index: "Very High (8.9 / 10)",
    growth_rate: "+24% Year-over-Year Demand",
    top_demanded_skills: [
      { skill: "TypeScript / React / Next.js", growth_pct: "+32%", demand_level: "Critical" },
      { skill: "Python / FastAPI / AI Integration", growth_pct: "+45%", demand_level: "Critical" },
      { skill: "Docker / Kubernetes Cloud Infra", growth_pct: "+28%", demand_level: "High" },
      { skill: "MongoDB / Redis Caching", growth_pct: "+19%", demand_level: "High" }
    ],
    salary_benchmarks: {
      entry: "$75,000 - $105,000",
      mid: "$115,000 - $155,000",
      senior: "$160,000 - $220,000+"
    }
  }
};

export const MOCK_REPORT: FullReport = {
  report_id: "REP-2026-8849",
  generated_at: "2026-07-29T08:00:00Z",
  overall_readiness_score: 86,
  target_role: "Full Stack Software Engineer",
  resume_intelligence: {
    overall_score: 85,
    impact_score: 82,
    formatting_score: 88,
    strengths: [
      "Clean technical skills organization across TypeScript, React, and Python",
      "Solid project section featuring modern stack (Next.js, FastAPI, MongoDB)",
      "Relevant education background with notable computer science coursework"
    ],
    weaknesses: [
      "Bullet points could incorporate more quantified business impact metrics",
      "Summary section is missing a clear personal value proposition"
    ],
    improvements: [
      "Quantify bullet points with STAR format metrics (e.g. 'Optimized SQL queries by 35%')",
      "Elevate bullet openings using high-impact verbs: 'Architected', 'Spearheaded'",
      "Add a 2-line Professional Summary tailored to target engineering roles"
    ],
    action_verb_rating: "Strong (78% high-impact verb frequency)"
  },
  ats_optimization: {
    match_score: 82,
    ats_compatibility: "High (91% ATS Pass Probability)",
    matched_keywords: ["TypeScript", "React", "Python", "FastAPI", "REST API", "Git", "Docker", "MongoDB"],
    missing_keywords: ["Kubernetes", "GraphQL", "Microservices Architecture", "Redis"],
    formatting_warnings: [
      "Ensure document uses standard single-column layout for ATS parser safety"
    ],
    bullet_optimizations: [
      {
        original: "Built frontend features using React and TypeScript for campus web app.",
        optimized: "Engineered responsive frontend UI components using React and TypeScript, boosting user engagement by 40%."
      },
      {
        original: "Worked on backend APIs with Python and FastAPI.",
        optimized: "Architected high-throughput REST APIs using FastAPI and Python, handling 10,000+ daily student requests."
      }
    ]
  },
  job_intelligence: {
    role_title: "Full Stack Software Engineer",
    seniority_level: "Junior / Entry-Level (0-2 YOE)",
    required_skills: ["Python", "FastAPI", "TypeScript", "React / Next.js", "MongoDB", "Git"],
    preferred_skills: ["Docker", "AWS / GCP", "Redis", "Tailwind CSS"],
    key_responsibilities: [
      "Develop scalable frontend components and backend RESTful APIs",
      "Participate in code reviews, sprint planning, and system architecture discussions",
      "Optimize application performance and integrate third-party web services"
    ],
    domain_focus: "Full Stack Web & Cloud Applications"
  },
  company_intelligence: {
    company_name: "Tech Global Unicorn",
    culture_highlights: [
      "Fast-paced product innovation culture with emphasis on engineering autonomy",
      "Strong focus on continuous learning, mentor pairings, and cross-functional hackathons"
    ],
    engineering_values: ["Customer-first engineering mindset", "High code quality and automated testing"],
    interview_style: "4-Round Loop: Tech Screening -> System Architecture -> Live Pair Coding -> Cultural Fit",
    recent_developments: ["Expanded engineering investments in cloud automation and AI agent integration"]
  },
  skill_gap_analysis: {
    critical_gaps: [
      { skill: "Docker & Containerization", urgency: "High", reason: "Required for modern deployment pipelines in 85% of listings" },
      { skill: "System Design Fundamentals", urgency: "High", reason: "Crucial for technical architecture interview rounds" }
    ],
    secondary_gaps: [
      { skill: "GraphQL APIs", urgency: "Medium", reason: "Increasingly used for client-side data fetching" }
    ],
    learning_pathway: [
      { week: "Week 1", topic: "Docker Containers & Compose", resource: "Docker Official Docs & Labs", estimated_hours: "6 hrs" },
      { week: "Week 2", topic: "System Design & Microservices", resource: "Designing Data-Intensive Applications", estimated_hours: "8 hrs" }
    ],
    overall_readiness_pct: 78
  },
  career_roadmap: {
    target_role: "Full Stack Software Engineer",
    career_trajectory: "Junior Software Engineer -> Full Stack Developer -> Senior Architect",
    expected_salary_range: "$85,000 - $115,000 / year",
    milestones: [
      {
        phase: "Days 1 - 30",
        title: "Foundation & Skill Blitz",
        duration: "Month 1",
        goals: ["Master Next.js App Router and FastAPI", "Build 1 full-stack app", "Optimize resume"],
        deliverables: ["Published GitHub repo", "ATS-compliant PDF resume"],
        key_metrics: "Resume ATS score >= 85%"
      },
      {
        phase: "Days 31 - 60",
        title: "Portfolio & Outreach",
        duration: "Month 2",
        goals: ["Launch recruiter outreach campaign", "Conduct mock interviews"],
        deliverables: ["30 custom outreach emails", "Refined 5 STAR stories"],
        key_metrics: "5+ recruiter responses"
      },
      {
        phase: "Days 61 - 90",
        title: "Interview Execution & Offer",
        duration: "Month 3",
        goals: ["Ace technical coding assessments", "Negotiate job offers"],
        deliverables: ["Signed offer letter for target software engineering role"],
        key_metrics: "1-2 formal job offers"
      }
    ]
  },
  market_trends: MOCK_ANALYTICS.market_trends,
  portfolio_recommendations: {
    portfolio_score: 88,
    project_ideas: [
      {
        title: "CampusOS AI - Multi-Agent Career Copilot",
        description: "Enterprise-grade AI platform coordinating 14 specialized agents for resume parsing, ATS scoring, and interview prep.",
        tech_stack: ["Next.js", "TypeScript", "FastAPI", "MongoDB", "Tailwind CSS"],
        difficulty: "Advanced",
        recruiter_appeal_score: 98,
        key_features: ["JWT Authentication", "Multi-Agent System Architecture", "Live Web Search via Tavily", "Downloadable PDF Reports"]
      }
    ]
  }
};
