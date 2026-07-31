from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class LinkedInProfileCompleteness(BaseModel):
    profile_score: float = 92.0
    missing_sections: List[str] = Field(default_factory=list)

class ThoughtLeadershipEngagement(BaseModel):
    posts_per_month: int = 4
    engagement_rate: float = 4.5

class BioHeadlineSEO(BaseModel):
    headline_score: float = 90.0
    detected_keywords: List[str] = Field(default_factory=list)

class CrossPlatformPresence(BaseModel):
    platforms_tracked: List[str] = Field(default_factory=list)
    presence_score: float = 85.0

class BrandConsistencyIndex(BaseModel):
    consistency_score: float = 88.0
    voice_alignment: str = "EXECUTIVE & TECHNICAL"

class MediaFeatureAudit(BaseModel):
    featured_articles_count: int = 2
    speaking_engagements_count: int = 1

class DeterministicBrandingPipelineResult(BaseModel):
    completeness: LinkedInProfileCompleteness
    engagement: ThoughtLeadershipEngagement
    headline: BioHeadlineSEO
    presence: CrossPlatformPresence
    consistency: BrandConsistencyIndex
    media: MediaFeatureAudit
    personal_brand_score: float
    confidence_score: float

class StrategicBrandNarrative(BaseModel):
    personal_brand_positioning: str
    target_thought_leadership_topics: List[str]

class ContentCalendarStrategy(BaseModel):
    recommended_post_topics: List[str]
    sample_linkedin_post_draft: str

class ReasoningBrandingPipelineResult(BaseModel):
    narrative: StrategicBrandNarrative
    content_calendar: ContentCalendarStrategy
    reasoning_steps: List[str]

class PersonalBrandingOrchestratorReport(BaseModel):
    department: str = "Personal Branding Intelligence"
    department_id: str = "dept_020"
    brand_strength_tier: str = "TOP TIER BRAND"
    personal_brand_score: float
    confidence_score: float
    deterministic_analysis: DeterministicBrandingPipelineResult
    reasoning_analysis: ReasoningBrandingPipelineResult
    reasoning_steps: List[str]
