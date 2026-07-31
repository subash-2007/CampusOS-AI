# CampusOS AI - Master Agent & Department Architecture Specification

## Overview
CampusOS AI is an enterprise-grade agentic AI operating system for higher education and career intelligence. The system consists of **111 Independent Departments**, housing exactly **1,111 Autonomous AI Agents** (111 Orchestrators + 222 Reasoning Agents + 777 Deterministic Agents + 1 Global Supervisor Agent), backed by shared infrastructure, deterministic data processing pipelines, LLM reasoning engines, and unified orchestrators.

---

## Department Structure Standard

Every department directory under `departments/<department_name>/` MUST strictly follow this standard structure:

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

---

## 10 Internal Agents Layout (per Department)

Each of the 111 departments contains exactly **10 specialized agents** categorized into:
1. **1 Master Orchestrator Agent**: Coordinates end-to-end pipeline execution, input validation, sub-agent invocation, data aggregation, and final synthesis.
2. **2 Reasoning Agents**: Perform deep contextual LLM analysis, narrative evaluation, qualitative recommendations, and strategic career planning.
3. **7 Deterministic Agents**: Perform fast, zero-stochasticity rule-based computational tasks, string parsing, regex extraction, keyword overlap indexing, and numerical scoring.

Total: **111 Departments &times; 10 Internal Agents + 1 Global Supervisor Agent = 1,111 Active AI Agents**.

---

## Shared Infrastructure (`departments/shared/`)

Duplicate logic across departments MUST be placed in `departments/shared/`:
- `scoring.py`: Normalized scoring engines, percentile calculators, and confidence matrices.
- `keywords.py`: TF-IDF keyword extraction, keyword overlap scoring, and technical dictionary matching.
- `prompts.py`: Prompt builder helpers, system role definitions, and structured prompt context formatting.
- `validators.py`: Data pattern validation, timeline date gap checking, and text sanity checks.

---

## Development & Execution Rules

1. **Zero Placeholder Code**: No `TODO`, `pass`, fake returns, or incomplete mock data.
2. **Dynamic Data Processing**: Every score, recommendation, and report MUST be computed dynamically from the user's uploaded resume and job description.
3. **Deterministic + Reasoning Synthesis**: Every department combines fast rule-based verification with high-level LLM reasoning.
4. **Traceable Reasoning Steps**: Every agent returns structured `reasoning_steps` explaining its decisions.
5. **Confidence Scores**: Every department calculates a numeric confidence score (0.0 to 1.0) based on input completeness and parsing certainty.
6. **Full Testability**: Every department MUST have pytest unit tests covering deterministic agents, reasoning agents, and the orchestrator. All 888 unit tests must pass cleanly.
