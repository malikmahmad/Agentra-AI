import time
from utils.antigravity import call_gemini

def run(extracted_content: str) -> dict:
    start = time.time()
    
    system = """You are an Insight & Contradiction Detection Agent.
    Your job:
    1. Find NON-OBVIOUS insights (not just summaries)
    2. Detect contradictions between data points
    3. Identify temporal anomalies
    4. Score source credibility (0-1)"""
    
    prompt = f"""
    Extracted Data: {extracted_content}
    
    Find deep insights. Detect any contradictions.
    """
    
    result = call_gemini(prompt, system)
    latency = (time.time() - start) * 1000
    
    return {
        "agent": "Insight Agent",
        "output": result,
        "latency_ms": latency,
        "status": "success"
    }
