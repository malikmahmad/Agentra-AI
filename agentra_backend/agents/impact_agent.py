import time
from utils.antigravity import call_gemini

def run(insights: str) -> dict:
    start = time.time()
    
    system = """You are a Business Impact Analysis Agent.
    For each insight, determine:
    - Financial impact
    - Operational impact
    - Risk level (low/medium/high/critical)
    - Time sensitivity
    - Affected stakeholders"""
    
    prompt = f"Insights: {insights}\n\nAnalyze all business impacts."
    
    result = call_gemini(prompt, system)
    latency = (time.time() - start) * 1000
    
    return {
        "agent": "Impact Agent",
        "output": result,
        "latency_ms": latency,
        "status": "success"
    }
