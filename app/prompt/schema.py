from typing import Any, Dict
from pydantic import BaseModel



class GenerateReportRequest(BaseModel):
    country: str
    project_budget: str
    category: str
    description: str
