import os
import json
import logging
from fhir_schemas import FHIRBundle
from mock_converter import get_mock_fhir_bundle

logger = logging.getLogger(__name__)

SAMPLE_CLINICAL_NOTE = """
Patient ETH-AFAR-042, a 28-year-old male, presents at the regional health center with a 4-week history of productive cough, 
low-grade evening fever, and unintended weight loss of 5kg. 
Physical examination: Pale conjunctivae, respiratory rate 22/min. BMI is 17.2 kg/m2 (moderate wasting).
Lab workup: Sputum GeneXpert assay confirms positive Mycobacterium tuberculosis, rifampicin resistance not detected. 
Diagnosis: Pulmonary Tuberculosis with concurrent undernutrition. Initiating Category 1 fixed-dose therapy.
"""

def extract_fhir_bundle(clinical_text: str = SAMPLE_CLINICAL_NOTE) -> FHIRBundle:
    api_key = os.getenv("GEMINI_API_KEY")
    use_mock = os.getenv("USE_MOCK_AGENT", "false").lower() == "true"

    if not api_key or use_mock:
        logger.info("Using Mock FHIR Converter (GEMINI_API_KEY unset or USE_MOCK_AGENT=true).")
        return get_mock_fhir_bundle()

    try:
        from google import genai
        from google.genai import types

        logger.info("Invoking Gemini 2.5 Flash for FHIR entity extraction...")
        client = genai.Client(api_key=api_key)
        prompt = (
            "You are a clinical health informatics agent. Convert this unstructured physician note into a "
            "standardized HL7 FHIR Bundle conforming strictly to the provided Pydantic schema:\n\n"
            f"{clinical_text}"
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=FHIRBundle,
                temperature=0.1
            )
        )
        # Compatible with both Pydantic v1 and v2
        if hasattr(FHIRBundle, "model_validate_json"):
            return FHIRBundle.model_validate_json(response.text)
        else:
            return FHIRBundle.parse_raw(response.text)
    except Exception as e:
        logger.warning(f"Live Gemini extraction failed ({e}). Reverting to mock FHIR converter.")
        return get_mock_fhir_bundle()

def main():
    print("--- Clinical FHIR Autonomous Agent ---")
    bundle = extract_fhir_bundle()
    
    out_file = "output/fhir_bundle_latest.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    
    # Serialize compatible with Pydantic v1 & v2
    if hasattr(bundle, "model_dump_json"):
        json_output = bundle.model_dump_json(indent=2)
    else:
        json_output = bundle.json(indent=2)
        
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(json_output)
        
    print(f"Extracted {len(bundle.conditions)} FHIR Conditions and {len(bundle.observations)} FHIR Observations.")
    print(f"Saved standardized FHIR bundle to: {out_file}")

if __name__ == "__main__":
    main()
