# CampusOS AI - Enterprise Agentic AI Operating System

![CampusOS Banner](https://img.shields.io/badge/CampusOS-AI_Operating_System-7c3aed?style=for-the-badge)
![111 Departments](https://img.shields.io/badge/Architecture-111_Departments-009688?style=for-the-badge)
![1,111 Agents](https://img.shields.io/badge/Active_Agents-1%2C111_AI_Agents-blue?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI_Python-009688?style=for-the-badge)
![Next.js 14](https://img.shields.io/badge/Frontend-Next.js_14_TypeScript-000000?style=for-the-badge)
![MongoDB](https://img.shields.io/badge/Database-MongoDB_Compass-47A248?style=for-the-badge)

CampusOS AI is an enterprise-grade agentic AI operating system for higher education and career intelligence. The system consists of **111 Independent AI Departments**, housing exactly **1,111 Autonomous AI Agents** (111 Master Orchestrators + 222 LLM Reasoning Agents + 777 Deterministic Agents + 1 Global Supervisor Agent), backed by shared infrastructure, deterministic data processing pipelines, LLM reasoning engines, and unified orchestrators.

---

## 🤖 Architecture Overview: 111 Departments & 1,111 AI Agents

Every single department directory under `departments/<department_name>/` adheres strictly to the **10-Agent Department Standard**:

```
departments/<department_name>/
├── __init__.py
├── schemas.py           # Pydantic data schemas, inputs, outputs, and intermediate states
├── deterministic.py     # 7 Rule-based deterministic agents (parsing, verification, metrics)
├── reasoning.py         # 2 LLM-driven reasoning agents (qualitative analysis, suggestions)
├── orchestrator.py      # 1 Master Orchestrator Agent uniting deterministic & reasoning pipelines
├── README.md            # Comprehensive documentation, API references, and architecture overview
└── tests/               # Department unit & integration test suite
    ├── __init__.py
    └── test_<department_name>.py
```

### 10 Internal AI Agents Layout per Department

1. **1 Master Orchestrator Agent**: Manages end-to-end pipeline execution, input validation, sub-agent invocation, data aggregation, and final synthesis.
2. **2 LLM Reasoning Agents**: Perform deep contextual LLM analysis, narrative evaluation, qualitative recommendations, and strategic career planning.
3. **7 Deterministic Agents**: Perform fast, zero-stochasticity rule-based computational tasks, string parsing, regex extraction, keyword overlap indexing, and numerical scoring.

**Total**: **111 Departments &times; 10 Internal Agents + 1 Global Supervisor Agent = 1,111 Active AI Agents**.

---

## 🏛️ 111 Departments Master Roster

### 1. Academic & Career Intelligence (`dept_001` → `dept_020`)
- `dept_001`: Resume Intelligence
- `dept_002`: ATS Optimization
- `dept_003`: Job Intelligence
- `dept_004`: Company Intelligence
- `dept_005`: Skill Gap Intelligence
- `dept_006`: Interview Intelligence
- `dept_007`: Career Roadmap
- `dept_008`: Career Analytics
- `dept_009`: Memory & Personalization
- `dept_010`: Market Trend Intelligence
- `dept_011`: Document Verification
- `dept_012`: Portfolio Intelligence
- `dept_013`: Communication Intelligence
- `dept_014`: Technical Skill Verification
- `dept_015`: Peer Benchmarking
- `dept_016`: Offer & Salary Negotiation
- `dept_017`: Alumni Network Intelligence
- `dept_018`: Mentorship Intelligence
- `dept_019`: Freelance & Gig Intelligence
- `dept_020`: Personal Branding Intelligence

### 2. Software Engineering & Infrastructure (`dept_021` → `dept_040`)
- `dept_021`: Leadership & Management Intelligence
- `dept_022`: Executive Communication
- `dept_023`: Startup & Entrepreneurship
- `dept_024`: Product Management Intelligence
- `dept_025`: Data Science & AI Intelligence
- `dept_026`: Cybersecurity & Compliance
- `dept_027`: Cloud & DevOps Engineering
- `dept_028`: Mobile App Development
- `dept_029`: UI/UX Design Intelligence
- `dept_030`: Software Architecture Intelligence
- `dept_031`: API Design Intelligence
- `dept_032`: Database Intelligence
- `dept_033`: Machine Learning Engineering
- `dept_034`: NLP Intelligence
- `dept_035`: Search & Recommendation Intelligence
- `dept_036`: Analytics Intelligence
- `dept_037`: Infrastructure Monitoring Intelligence
- `dept_038`: Content Intelligence
- `dept_039`: User Onboarding Intelligence
- `dept_040`: Notification Intelligence

### 3. Enterprise Operations & Support (`dept_041` → `dept_060`)
- `dept_041`: Privacy & Data Governance
- `dept_042`: Performance Optimization Intelligence
- `dept_043`: Testing & Quality Assurance Intelligence
- `dept_044`: Internationalization & Localization Intelligence
- `dept_045`: Accessibility & Inclusivity Intelligence
- `dept_046`: Billing & Monetization Intelligence
- `dept_047`: Customer Support & Success Intelligence
- `dept_048`: Sales & Revenue Intelligence
- `dept_049`: Partner & Ecosystem Intelligence
- `dept_050`: Learning & Course Intelligence
- `dept_051`: Assessment & Certification Intelligence
- `dept_052`: Internship & Co-op Intelligence
- `dept_053`: University & Campus Relations
- `dept_054`: Academic Advising Intelligence
- `dept_055`: Student Financial Aid Intelligence
- `dept_056`: Research & Publication Intelligence
- `dept_057`: Campus Housing & Facilities Intelligence
- `dept_058`: Student Health & Wellness Intelligence
- `dept_059`: Global Study Abroad Intelligence
- `dept_060`: Alumni Mentorship & Engagement

### 4. Student Services, Campus Life & Governance (`dept_061` → `dept_111`)
- `dept_061` to `dept_080`: Parent Relations, K-12 Outreach, Transfer Students, Executive Ed, Campus Safety, Disability Services, Veterans, Dining, Athletics, Bookstore, Parking, Legal Services, Childcare, DEI, Student Govt, Greek Life, Campus Events, Sustainability, Institutional Advancement, Alumni Career.
- `dept_081` to `dept_100`: Auxiliary Enterprises, Residential Housing, Health & Counseling, Campus Rec, Student Employment, Registrar, Admissions, Orientation, Judicial & Conduct, Culinary, Disability Access, IT Services, Institutional Research, Faculty Development, Mental Health, Library Commons, Innovation Incubator.
- `dept_101` to `dept_111`: Global Engagement, Security Operations, EHS Compliance, Capital Construction, Civic Engagement, Endowment Management, NCAA Athletics, Auxiliary Housing, Procurement Purchasing, HR Talent Operations, Executive Board Governance.

---

## 🛠️ Project Structure

```
CampusOS/
├── backend/
│   ├── app/
│   │   ├── api/                  # FastAPI REST routes (agents, auth, supervisor, chat, etc.)
│   │   ├── agents/               # Dynamic Agent Registry & Supervisor Pipeline Engine
│   │   ├── core/                 # Config, Security JWT, and MongoDB Database Manager
│   │   └── main.py               # FastAPI application entrypoint
│   ├── requirements.txt          # Python dependencies
├── departments/                  # 111 Independent AI Departments (1,110 internal AI agents)
│   ├── dept_001/ ... dept_111/
│   └── shared/                   # Shared scoring, validators, prompts & keywords utilities
├── frontend/
│   ├── src/
│   │   ├── app/                  # Next.js 14 App Router pages & Enterprise Dashboard
│   │   ├── components/           # UI design system & Dashboard components
│   │   └── lib/                  # API client, Zustand store, PDF generator, TypeScript types
│   └── package.json              # Frontend dependencies
├── scripts/                      # Verification scripts & scaffold utilities
├── AGENTS.md                     # Master Agent & Department Architecture Specification
├── DEPARTMENTS_REGISTRY.md       # Complete 111 Departments Registry
├── PROGRESS.md                   # System Build Progress & Verification Metrics
└── README.md                     # Project documentation
```

---

## 🚀 Quick Setup & Installation Guide

### Prerequisites
- Node.js (v18+) & npm
- Python (v3.10+)
- MongoDB (Compass for local development on `mongodb://localhost:27017` or Atlas cloud instance)

---

### Step 1: Start Backend (FastAPI)

```bash
cd backend

# Create virtual environment (optional)
python -m venv venv
# Windows:
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
Backend server will run at: `http://localhost:8000`  
API Documentation (Swagger UI): `http://localhost:8000/docs`  
Department API Endpoint: `http://localhost:8000/api/v1/agents/departments`

---

### Step 2: Start Frontend (Next.js)

Open a new terminal window:

```bash
cd frontend

# Install packages
npm install

# Start Next.js development server
npm run dev
```
Frontend Web App will run at: `http://localhost:3000`  
Enterprise Dashboard: `http://localhost:3000/dashboard`  
Agents Directory: `http://localhost:3000/dashboard/agents`

---

### Step 3: Run Whole System Verification

```bash
# Run system audit across all 111 departments and Supervisor Agent:
python scripts/verify_whole_project.py
```
Outputs: `111/111 Departments Passed Import & Execution Audit.`
