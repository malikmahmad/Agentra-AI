def generate_email(action_text: str) -> str:
    return f"""Subject: [URGENT] Agentra AI Action Report

Dear Stakeholder,

Our AI monitoring system has detected a critical situation.

RECOMMENDED ACTIONS:
{action_text}

Projected Impact: High revenue recovery.
This is an automated message from Agentra AI System.

Regards,
Agentra Autonomous Agent"""
