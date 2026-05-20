from pydantic import BaseModel
from typing import List, Optional, Any, Dict

class AnalyzeRequest(BaseModel):
    text: str
    input_type: Optional[str] = "news"

class AgentLog(BaseModel):
    agent: str
    status: str
    output: Any
    latency_ms: float

class SimulationResult(BaseModel):
    before_state: Dict
    after_state: Dict
    actions_executed: List[str]
    email_draft: str
    crm_update: Dict
    logs: List[str]
    latency_ms: float
    status: str
