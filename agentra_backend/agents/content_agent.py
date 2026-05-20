import time
from utils.antigravity import call_gemini

def run(raw_content: str, input_type: str) -> dict:
    start = time.time()
    
    system = """You are a Content Extraction Agent. 
    Extract: key facts, entities, numbers, dates, signals.
    Remove noise. Return a structured summary of the content."""
    
    prompt = f"""
    Input Type: {input_type}
    Content: {raw_content[:3000]}
    
    Extract all meaningful information. Ignore irrelevant noise.
    """
    
    result = call_gemini(prompt, system)
    latency = (time.time() - start) * 1000
    
    return {
        "agent": "Content Agent",
        "output": result,
        "latency_ms": latency,
        "status": "success"
    }
