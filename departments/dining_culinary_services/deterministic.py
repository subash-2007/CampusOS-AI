from departments.shared.scoring import ScoringEngine
from departments.dining_culinary_services.schemas import (
    CulinaryMenuRecipeRotationMetric, ExecutiveChefStaffingCertAudit, FarmToTableLocalSourcingMetric,
    SpecialtyDietaryStationAudit, CulinaryTasteTestCSATAudit, CulinaryEventThemeNightMetric, DeterministicCulinaryPipelineResult
)

class CulinaryMenuRecipeRotationMeterAgent:
    """Agent 1: Measures unique recipes served, seasonal menu rotations, and culinary diversity score percentage."""
    def run(self, recipes: int = 1450) -> CulinaryMenuRecipeRotationMetric:
        return CulinaryMenuRecipeRotationMetric(unique_recipes_served_per_semester=recipes, seasonal_menu_rotations_count=4, culinary_diversity_score_pct=94.8)

class ExecutiveChefStaffingCertAuditorAgent:
    """Agent 2: Audits certified executive chefs count, ServSafe manager certification percentage, and staff training hours."""
    def run(self) -> ExecutiveChefStaffingCertAudit:
        return ExecutiveChefStaffingCertAudit(certified_executive_chefs_count=18, servsafe_manager_certification_pct=100.0, culinary_staff_training_hours_annual=4200)

class FarmToTableLocalSourcingMeterAgent:
    """Agent 3: Measures local farm partnerships, sustainable seafood procurement percentage, and organic spend percentage."""
    def run(self) -> FarmToTableLocalSourcingMetric:
        return FarmToTableLocalSourcingMetric(local_farm_partnerships_count=38, sustainable_seafood_procurement_pct=88.5, organic_produce_spend_pct=32.4)

class SpecialtyDietaryStationAuditorAgent:
    """Agent 4: Audits gluten-free kitchens, top-9 allergen-free stations, and dietitian-approved recipe percentage."""
    def run(self) -> SpecialtyDietaryStationAudit:
        return SpecialtyDietaryStationAudit(gluten_free_dedicated_kitchens=4, top_9_allergen_free_stations=6, dietitian_approved_recipe_pct=98.2)

class CulinaryTasteTestCSATAuditorAgent:
    """Agent 5: Audits student culinary taste CSAT score and dining hall feedback submissions count."""
    def run(self) -> CulinaryTasteTestCSATAudit:
        return CulinaryTasteTestCSATAudit(student_culinary_taste_csat_score=4.78, dining_hall_feedback_submissions_annual=14200)

class CulinaryEventThemeNightMeterAgent:
    """Agent 6: Measures theme night culinary events count and average theme night attendees."""
    def run(self) -> CulinaryEventThemeNightMetric:
        return CulinaryEventThemeNightMetric(theme_night_culinary_events_annual=48, theme_night_attendees_average=3200)

class DiningCulinaryServicesScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Dining Culinary Services."""
    def __init__(self):
        self.menus_agent = CulinaryMenuRecipeRotationMeterAgent()
        self.chefs_agent = ExecutiveChefStaffingCertAuditorAgent()
        self.farm_agent = FarmToTableLocalSourcingMeterAgent()
        self.dietary_agent = SpecialtyDietaryStationAuditorAgent()
        self.csat_agent = CulinaryTasteTestCSATAuditorAgent()
        self.events_agent = CulinaryEventThemeNightMeterAgent()

    def run(self, recipes: int = 1450) -> DeterministicCulinaryPipelineResult:
        menus = self.menus_agent.run(recipes)
        chefs = self.chefs_agent.run()
        farm_to_table = self.farm_agent.run()
        dietary = self.dietary_agent.run()
        csat = self.csat_agent.run()
        events = self.events_agent.run()

        metrics = {
            "servsafe_cert": chefs.servsafe_manager_certification_pct,
            "dietitian_approved": dietary.dietitian_approved_recipe_pct,
            "diversity_score": menus.culinary_diversity_score_pct,
            "taste_csat": (csat.student_culinary_taste_csat_score / 5.0) * 100
        }
        weights = {"servsafe_cert": 0.35, "dietitian_approved": 0.30, "diversity_score": 0.20, "taste_csat": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(menus.unique_recipes_served_per_semester, 100)
        return DeterministicCulinaryPipelineResult(
            menus=menus, chefs=chefs, farm_to_table=farm_to_table,
            dietary=dietary, csat=csat, events=events,
            culinary_score=score, confidence_score=confidence
        )
