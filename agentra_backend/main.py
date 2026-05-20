from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import vertexai
from vertexai.generative_models import GenerativeModel
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Vertex AI Constants
PROJECT_ID = "starlit-lotus-469819-s5"
LOCATION = "us-central1"
KEY_PATH = os.path.join(os.path.dirname(__file__), "service-account-key.json")

if os.path.exists(KEY_PATH):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH

# Lazy Loader for Vertex AI
model = None
def get_model():
    global model
    if model is None:
        try:
            vertexai.init(project=PROJECT_ID, location=LOCATION)
            model = GenerativeModel("gemini-2.5-flash")
        except Exception as e:
            print(f"Vertex AI Lazy Init failed: {e}")
    return model

class AnalyzeRequest(BaseModel):
    text: str

def generate(prompt):
    m = get_model()
    if not m:
        return "Error: Vertex AI Model not initialized."
    try:
        r = m.generate_content(prompt)
        return r.text
    except Exception as e:
        return f"Error during generation: {str(e)}"

def content_agent(text):
    return generate(f"""You are a Content Analysis Agent for Agentra AI System.
Extract key facts, numbers, regions, products, and signals from this report.
Identify source credibility and timestamp if available.
Return as clear bullet points:
{text}""")

def insight_agent(facts):
    return generate(f"""You are an Insight Agent for Agentra AI System.
From these facts, identify the most important business insight.
Detect any contradictions between data sources.
Score each source credibility (High/Medium/Low):
{facts}""")

def impact_agent(insight):
    return generate(f"""You are an Impact Analysis Agent for Agentra AI System.
Analyze business impact:
- Revenue impact
- Operations impact
- Customer impact
- Contradiction resolution
- Temporal analysis
{insight}""")

def action_agent(impact):
    return generate(f"""You are an Action Planning Agent for Agentra AI System.
Generate exactly 5 interconnected actions with constraints.
Format:
Action 1: [name] - Budget: [X PKR] - Urgency: [High/Medium/Low] - Time: [X hours]

Action 2: ...
Each action must depend on previous one.
{impact}""")

def simulate_agent(action):
    return generate(f"""You are a Simulation Agent for Agentra AI System.
Simulate execution of these actions. Show:

BEFORE STATE:
- Current system status

ACTION EXECUTION LOG:
- Action 1: [status] [timestamp]
- Action 2: [status] [timestamp]
- Action 3: [status] [timestamp]
- Action 4: [status] [timestamp]
- Action 5: [status] [timestamp]

FAILURE SIMULATION:
- Simulate one action failing and recovery

AFTER STATE:
- Updated system status

MOCK CRM UPDATE:
- Campaign created

EMAIL DRAFT:
- Subject and body

COST ESTIMATE:
- Total cost in PKR

PROJECTED IMPACT:
- Expected outcome
{action}""")

@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    trace = []
    
    # Run the pipeline
    facts = content_agent(req.text)
    trace.append({"agent": "Content Agent", "status": "complete", "output": facts})
    
    insight = insight_agent(facts)
    trace.append({"agent": "Insight Agent", "status": "complete", "output": insight})
    
    impact = impact_agent(insight)
    trace.append({"agent": "Impact Agent", "status": "complete", "output": impact})
    
    action = action_agent(impact)
    trace.append({"agent": "Action Agent", "status": "complete", "output": action})
    
    simulation = simulate_agent(action)
    trace.append({"agent": "Simulation Agent", "status": "complete", "output": simulation})
    
    return {
        "trace": trace,
        "insight": insight,
        "impact": impact,
        "action": action,
        "simulation": simulation,
        "timestamp": datetime.now().isoformat(),
        "status": "success"
    }

@app.get("/")
def root():
    return {"status": "Agentra Backend Running - Powered by Google Vertex AI!", "version": "2.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    