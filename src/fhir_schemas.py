from typing import List, Optional
from pydantic import BaseModel, Field

class Coding(BaseModel):
    system: str
    code: str
    display: str

class CodeableConcept(BaseModel):
    coding: List[Coding]
    text: Optional[str] = None

class FHIRCondition(BaseModel):
    resourceType: str = "Condition"
    id: str
    clinicalStatus: str = "active"
    code: CodeableConcept
    subject: str = Field(description="Patient reference e.g. Patient/P001")
    note: Optional[str] = None

class FHIRObservation(BaseModel):
    resourceType: str = "Observation"
    id: str
    status: str = "final"
    code: CodeableConcept
    subject: str
    valueString: Optional[str] = None
    valueQuantity: Optional[dict] = None

class FHIRBundle(BaseModel):
    resourceType: str = "Bundle"
    type: str = "collection"
    total_entries: int
    conditions: List[FHIRCondition]
    observations: List[FHIRObservation]
