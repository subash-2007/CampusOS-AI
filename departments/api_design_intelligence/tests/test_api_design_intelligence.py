import pytest, asyncio
from departments.api_design_intelligence.deterministic import (
    RESTEndpointAuditorAgent, OpenAPISpecCoverageAgent, APIResponseTimeMeterAgent,
    RateLimitingAuditorAgent, APIAuthenticationAuditorAgent, APIErrorResponseStandardAgent, APIScorerAgent
)
from departments.api_design_intelligence.orchestrator import APIDesignOrchestratorAgent

def test_rest_endpoint_auditor():
    res = RESTEndpointAuditorAgent().run(42)
    assert res.versioned_endpoints_pct == 100.0
    assert res.non_restful_patterns_count == 0

def test_openapi_spec_coverage():
    res = OpenAPISpecCoverageAgent().run(98.0)
    assert res.spec_coverage_pct >= 95.0

def test_api_response_time_meter():
    res = APIResponseTimeMeterAgent().run(120)
    assert res.latency_tier == "EXCELLENT"

def test_rate_limiting_auditor():
    res = RateLimitingAuditorAgent().run()
    assert res.rate_limit_headers_present is True

def test_api_authentication_auditor():
    res = APIAuthenticationAuditorAgent().run()
    assert "JWT" in res.auth_scheme

def test_api_error_response_standard():
    res = APIErrorResponseStandardAgent().run()
    assert res.uses_rfc7807_format is True

def test_api_scorer():
    res = APIScorerAgent().run(42, 98.0)
    assert res.api_quality_score >= 85.0
    assert res.confidence_score >= 0.5

def test_api_design_orchestrator():
    report = asyncio.run(APIDesignOrchestratorAgent().run_pipeline(42, 98.0))
    assert report.department == "API Design Intelligence"
    assert report.department_id == "dept_031"
    assert report.api_tier == "PRODUCTION GRADE API"
    assert len(report.reasoning_steps) == 4
