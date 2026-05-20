import time
from utils.antigravity import call_gemini

def run(impacts: str) -> dict:
    start = time.time()
    
    system = """You are a Strategic Action Planning Agent.
    Generate a CHAIN of 5 connected actions.
    Each action must:
    - Have a clear trigger condition
    - Reference the previous action's outcome
    - Be realistic and executable
    - Have measurable success criteria"""
    
    prompt = f"""
    Impact Analysis: {impacts}
    
    Generate a realistic 5-step action chain.
    """
    
    result = call_gemini(prompt, system)
    latency = (time.time() - start) * 1000
    
    return {
        "agent": "Action Agent",
        "output": result,
        "latency_ms": latency,
        "status": "success"
    }
