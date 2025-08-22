from typing import Any, Dict
from pydantic import BaseModel



class GenerateReportRequest(BaseModel):
    country: str
    project_budget: float
    category: str
    description: str
    language: str
