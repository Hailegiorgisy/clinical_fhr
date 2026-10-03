# clinical-fhir-agent: Autonomous Clinical Documentation to HL7 FHIR Conversion

An autonomous clinical informatics agent that transforms unstructured physician consultation notes into strictly validated HL7 FHIR (Fast Healthcare Interoperability Resources) JSON bundles.

## Key Capabilities
- **Strict Pydantic R4 Schemas**: Enforces standard `Condition`, `Observation`, and `CodeableConcept` structures with ICD-10 and LOINC codings.
- **LLM Orchestration**: Employs Gemini 2.5 Flash with structured schema decoders.
- **Offline Mock Adapter**: Includes zero-dependency mock converter allowing tests and CI suites to execute reliably without live credentials.

## Quickstart
```bash
python src/agent.py
```
