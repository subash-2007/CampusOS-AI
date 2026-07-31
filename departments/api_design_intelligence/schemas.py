from typing import List, Optional
from pydantic import BaseModel, Field

class RESTEndpointAudit(BaseModel):
    total_endpoints: int = 42
    versioned_endpoints_pct: float = 100.0
    non_restful_patterns_count: int = 0

class OpenAPISpecCoverage(BaseModel):
    spec_coverage_pct: float = 98.0
    missing_schema_definitions: int = 0

class APIResponseTimeMetric(BaseModel):
    p50_latency_ms: int = 45
    p99_latency_ms: int = 120
    latency_tier: str = "EXCELLENT"

class RateLimitingAudit(BaseModel):
    rate_limit_headers_present: bool = True
    requests_per_minute_limit: int = 1000

class APIAuthenticationAudit(BaseModel):
    auth_scheme: str = "OAuth2 + JWT RS256"
    token_expiry_minutes: int = 60
    refresh_token_rotation: bool = True

class APIErrorResponseStandard(BaseModel):
    uses_rfc7807_format: bool = True
    error_code_coverage_pct: float = 96.0

class DeterministicAPIPipelineResult(BaseModel):
    endpoint_audit: RESTEndpointAudit
    openapi: OpenAPISpecCoverage
    latency: APIResponseTimeMetric
    rate_limit: RateLimitingAudit
    auth: APIAuthenticationAudit
    error_standard: APIErrorResponseStandard
    api_quality_score: float
    confidence_score: float

class StrategicAPINarrative(BaseModel):
    api_design_summary: str
    key_api_strengths: List[str]

class APIEvolutionPlan(BaseModel):
    versioning_strategy: List[str]
    sample_openapi_yaml: str

class ReasoningAPIPipelineResult(BaseModel):
    narrative: StrategicAPINarrative
    evolution_plan: APIEvolutionPlan
    reasoning_steps: List[str]

class APIDesignOrchestratorReport(BaseModel):
    department: str = "API Design Intelligence"
    department_id: str = "dept_031"
    api_tier: str = "PRODUCTION GRADE API"
    api_quality_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAPIPipelineResult
    reasoning_analysis: ReasoningAPIPipelineResult
    reasoning_steps: List[str]
