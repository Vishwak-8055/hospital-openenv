from pydantic import BaseModel
from typing import List

class Patient(BaseModel):
    id: int
    severity: float
    wait_time: int
    condition: str

class Resources(BaseModel):
    icu_beds: int
    doctors: int

class State(BaseModel):
    patients: List[Patient]
    resources: Resources