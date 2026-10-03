from fhir_schemas import FHIRBundle, FHIRCondition, FHIRObservation, CodeableConcept, Coding

def get_mock_fhir_bundle() -> FHIRBundle:
    return FHIRBundle(
        total_entries=3,
        conditions=[
            FHIRCondition(
                id="cond-tb-001",
                clinicalStatus="active",
                code=CodeableConcept(
                    coding=[Coding(system="http://hl7.org/fhir/sid/icd-10", code="A15.0", display="Tuberculosis of lung")],
                    text="Pulmonary Tuberculosis"
                ),
                subject="Patient/ETH-AFAR-042",
                note="Patient presenting with chronic cough, night sweats, and localized rales."
            )
        ],
        observations=[
            FHIRObservation(
                id="obs-bmi-001",
                status="final",
                code=CodeableConcept(
                    coding=[Coding(system="http://loinc.org", code="39156-5", display="Body mass index")],
                    text="Body Mass Index"
                ),
                subject="Patient/ETH-AFAR-042",
                valueQuantity={"value": 17.2, "unit": "kg/m2", "system": "http://unitsofmeasure.org", "code": "kg/m2"}
            ),
            FHIRObservation(
                id="obs-sputum-002",
                status="final",
                code=CodeableConcept(
                    coding=[Coding(system="http://loinc.org", code="88224-1", display="GeneXpert MTB/RIF")],
                    text="GeneXpert MTB assay"
                ),
                subject="Patient/ETH-AFAR-042",
                valueString="MTB Detected; Rifampicin Resistance NOT Detected"
            )
        ]
    )
