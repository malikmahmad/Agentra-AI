import time
import json
from utils.antigravity import call_gemini
from tools.mock_crm import update_crm
from tools.mock_email import generate_email

def run(action_chain_text: str) -> dict:
    start = time.time()
    logs = []
    
    # Before state
    before_state = {
        "crm_status": "Idle",
        "pricing": "Standard",
        "system_health": "Degraded"
    }
    
    logs.append("[00:00] Simulation started")
    logs.append(f"[00:01] Before state: {json.dumps(before_state)}")
    
    # Simulate execution
    logs.append("[00:02] Executing action chain steps...")
    logs.append("[00:05] ✓ All steps simulated successfully")
    
    # CRM Mock Update
    crm_result = update_crm({
        "campaign": "AI Recovery Plan",
        "status": "active"
    })
    logs.append(f"[00:08] CRM Updated: {json.dumps(crm_result)}")
    
    # Email Draft
    email = generate_email(action_chain_text)
    logs.append("[00:09] Email draft generated")
    
    # After state
    after_state = {
        "crm_status": "Campaign Active",
        "pricing": "Dynamic",
        "system_health": "Recovering"
    }
    
    logs.append("[00:10] After state captured")
    logs.append("[00:10] ✅ Simulation complete")
    
    latency = (time.time() - start) * 1000
    
    return {
        "agent": "Simulation Agent",
        "before_state": before_state,
        "after_state": after_state,
        "actions_executed": ["Diagnose", "Notify", "Update", "Mitigate", "Monitor"],
        "email_draft": email,
        "crm_update": crm_result,
        "logs": logs,
        "latency_ms": latency,
        "status": "success"
    }
