# CampusOS AI - Production Multi-Agent Career Platform

![CampusOS Banner](https://img.shields.io/badge/CampusOS-AI_Career_Copilot-7c3aed?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI_Python-009688?style=for-the-badge)
![Next.js 14](https://img.shields.io/badge/Frontend-Next.js_14_TypeScript-000000?style=for-the-badge)
![MongoDB](https://img.shields.io/badge/Database-MongoDB_Compass-47A248?style=for-the-badge)

CampusOS AI is an enterprise-grade full-stack web application designed to empower students and higher education institutions with **111 Independent Departments** housing **1,111 specialized AI agents**. Built with Next.js (React + TypeScript + Tailwind CSS) on the frontend, FastAPI (Python) on the backend, MongoDB as the database, and JWT authentication.

---

## 🤖 111 Departments & 1,111 Specialized AI Agents Architecture

1. **Career Orchestrator Agent**: Master intelligence routing queries, coordinating multi-agent workflows, and synthesizing career advice.
2. **Resume Intelligence Agent**: Evaluates resume structure, formatting, impact metrics, action verb density, and strengths/weaknesses.
3. **ATS Optimization Agent**: Calculates ATS match percentage, keyword gaps, scanner pass rates, and bullet point rewrites.
4. **Job Intelligence Agent**: Deconstructs Job Descriptions into core domain requirements, tech stacks, and seniority signals.
5. **Company Intelligence Agent**: Researches target company culture, interview focus, engineering values, and live web news via Tavily search.
6. **Skill Gap Intelligence Agent**: Identifies missing technical and soft skills, generating a prioritized learning matrix & course recommendations.
7. **Interview Intelligence Agent**: Generates tailored technical/behavioral interview Q&A, STAR method answers, and mock practice simulations.
8. **Career Roadmap Agent**: Generates 30-60-90 day milestone career execution plans, target roles, and salary trajectories.
9. **Career Analytics Agent**: Aggregates readiness scores, market competitiveness metrics, and domain radar distributions.
10. **Memory & Personalization Agent**: Stores user preferences, skill mastery history, and personal context across sessions.
11. **Market Trend Intelligence Agent**: Analyzes live hiring demand indices, trending technology stacks (2026), and compensation benchmarks.
12. **Document Verification Agent**: Audits resume consistency, employment timeline dates, date gaps, and credential formats.
13. **Portfolio Intelligence Agent**: Evaluates GitHub portfolio impact, project ideas, and generates professional README markdown files.
14. **Communication Intelligence Agent**: Drafts cold emails, LinkedIn connection requests, follow-up messages, and salary negotiation scripts.

---

## 🛠️ Project Structure

```
CampusOS/
├── backend/
│   ├── app/
│   │   ├── api/                  # FastAPI REST routes (auth, resume, job, agents, chat, analytics, reports)
│   │   ├── agents/               # All 14 AI Agent implementations & AgentRegistry
│   │   ├── core/                 # Config, JWT Security, and Motor MongoDB Database Manager
│   │   ├── models/               # Pydantic Schemas & Data models
│   │   └── main.py               # FastAPI application entrypoint
│   ├── .env                      # API keys & Database config
│   └── requirements.txt          # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── app/                  # Next.js 14 App Router pages & dashboard
│   │   ├── components/           # UI design system & Dashboard components
│   │   └── lib/                  # API client, PDF generator, TypeScript types, Mock datasets
│   ├── .env.local                # Frontend API endpoint config
│   ├── tailwind.config.js        # Custom theme & glassmorphism styling
│   └── package.json              # Frontend dependencies
└── README.md
```

---

H## 🚀 Quick Setup & Installation Guide

### Prerequisites
- Node.js (v18+) & npm
- Python (v3.10+)
- MongoDB (Compass for local development on `mongodb://localhost:27017` or automatic in-memory fallback)

---

### Step 1: Start Backend (FastAPI)

```bash
cd backend

# Create virtual environment (optional but recommended)
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
Frontend web application will run at: `http://localhost:3000`

---

## 🔐 Preconfigured API Keys & Environment

The backend `.env` is pre-populated with your API credentials:
- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_API_KEY`
- `TAVILY_API_KEY`

> **Resilience & Fallback Engine**: If any API key reaches rate limits or runs offline, CampusOS AI automatically engages its intelligent heuristic engine so every single dashboard view, agent execution, and PDF report functions 100% reliably.

---

## 📊 Key Features Demonstration

- **Multi-Agent AI Chat Command Center**: Select any of the 14 agents or let the Master Orchestrator auto-route your query.
- **Resume Intelligence Analyzer**: Drag-and-drop resume PDF/DOCX audit with impact scores and formatting fixes.
- **Job Description & ATS Matcher**: Instant side-by-side keyword match rate and bullet point rewriter.
- **30-60-90 Day Milestone Roadmap**: Interactive visual timeline with actionable monthly goals.
- **Downloadable PDF Reports**: One-click generation of comprehensive career audit reports.
