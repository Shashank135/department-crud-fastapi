from pydantic import BaseModel, Field # type: ignore
from typing import Optional
from uuid import uuid4

class Department(BaseModel):
    department_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    code: str
    facility_id: str
    active_status: bool
