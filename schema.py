from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class CalculateRequest(BaseModel):
    image: str
    dict_of_vars: Optional[Dict[str, Any]]


class CalculateResponse(BaseModel):
    message: str
    success: bool
    data: Optional[List[Dict[str, Any]]] = None
