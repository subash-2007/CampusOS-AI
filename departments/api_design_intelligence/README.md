# Department 031: API Design Intelligence (`api_design_intelligence`)

## Overview
Audits REST endpoint naming/versioning, OpenAPI 3.1 spec coverage, P99 latency, rate limiting, OAuth2 JWT authentication, and RFC 7807 error standards. Generates API versioning strategies and OpenAPI YAML samples.

## 10-Agent Architecture
### Deterministic (7)
1. RESTEndpointAuditorAgent, 2. OpenAPISpecCoverageAgent, 3. APIResponseTimeMeterAgent,
4. RateLimitingAuditorAgent, 5. APIAuthenticationAuditorAgent, 6. APIErrorResponseStandardAgent,
7. APIScorerAgent
### Reasoning (2)
8. StrategicAPINarrativeAgent, 9. APIEvolutionPlannerAgent
### Orchestrator (1)
10. APIDesignOrchestratorAgent
