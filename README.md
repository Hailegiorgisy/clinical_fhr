# Clinical FHIR Agent

An autonomous clinical informatics agent that converts unstructured physician consultation notes into structured HL7 FHIR JSON bundles.

## Project Overview

This project focuses on transforming physician documentation into standardized healthcare data models that can be exchanged across systems. It uses schema-driven extraction to ensure valid FHIR representations for conditions, observations, and coded medical concepts.

## Key Capabilities

- Strict Pydantic R4 schema validation
- Conversion of physician notes into HL7 FHIR-compliant bundles
- ICD-10 and LOINC-aware coding support
- LLM-powered structured extraction with validation
- Mock adapter for offline testing and CI execution
- Designed for clinical data interoperability pipelines

## Why It Matters

Clinical documentation is often free-text and inconsistent. This project helps standardize notes into interoperable FHIR resources, improving data quality, analysis, and exchange between healthcare information systems.

## Core Features

- `Condition` extraction from consultation notes
- `Observation` generation for symptoms and findings
- `CodeableConcept` validation with standard medical coding
- Structured conversion pipeline for downstream analytics
- Safe, testable conversion logic without requiring live credentials

## Installation

```bash
git clone https://github.com/Hailegiorgisy/clinical_fhr.git
cd clinical_fhr
python -m pip install -r requirements.txt
```

## Quickstart

```bash
python src/agent.py
```

## Example Workflow

1. Pass a physician consultation note into the agent
2. Extract relevant findings, diagnoses, and observations
3. Map concepts to FHIR-compatible code systems
4. Validate the generated record against Pydantic R4 models
5. Output a clean HL7 FHIR JSON bundle

## Example Input

```text
Patient presents with fever, cough, and shortness of breath for three days.
Past medical history includes asthma.
```

## Example Output

The system produces a FHIR JSON structure containing validated resources such as:

- `Condition`
- `Observation`
- `Coding`
- `CodeableConcept`
- Resource bundles suitable for interoperability workflows

## Repository Structure

```text
clinical_fhr/
├── src/
├── tests/
├── data/
├── README.md
├── requirements.txt
└── .env.example
```

## Mock Adapter

The project includes a zero-dependency mock conversion adapter that can be used in development and CI so tests run reliably without live external services or credentials.

## Technical Notes

- Schema validation is enforced to maintain standard compliance
- Outputs are structured to reduce downstream interoperability issues
- The project is suitable for research prototypes, clinical NLP workflows, and EHR integration testing

## Contributing

Contributions are welcome for improving clinical extraction quality, expanding code mapping coverage, and strengthening validation logic.

## License

This project is open-source and distributed under the MIT license unless otherwise specified in the repository.
