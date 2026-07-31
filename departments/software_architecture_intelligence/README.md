# Department 030: Software Architecture Intelligence (`software_architecture_intelligence`)

## Overview
The **Software Architecture Intelligence Department** delivers an enterprise multi-agent pipeline designed to measure function cyclomatic complexity, audit package afferent/efferent coupling & instability indexes, identify GoF design patterns (Repository, Orchestrator, Factory, Strategy), evaluate microservice boundary decoupling, meter AST code duplication percentages, benchmark system throughput QPS scalability, and generate C4 Mermaid architecture diagrams.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **CyclomaticComplexityMeterAgent**: Measures function cyclomatic complexity.
2. **CouplingCohesionAuditorAgent**: Audits afferent/efferent coupling and instability.
3. **DesignPatternCoverageAgent**: Identifies GoF design pattern implementations.
4. **MicroserviceBoundaryMeterAgent**: Evaluates microservice domain boundaries.
5. **CodeDuplicationIndexAgent**: Measures code duplication percentages using AST.
6. **SystemScalabilityBenchmarkAgent**: Models QPS throughput limits and auto-scaling.
7. **ArchitectureScorerAgent**: Master deterministic aggregator for software architecture metrics.

### Reasoning Agents (2)
8. **StrategicArchitectureNarrativeAgent**: Formulates strategic software architecture reviews.
9. **ArchitecturalRefactoringPlannerAgent**: Formulates refactoring roadmaps and Mermaid diagrams.

### Orchestrator Agent (1)
10. **SoftwareArchitectureOrchestratorAgent**: Master Orchestrator Agent uniting architectural health scores and refactoring plans.
