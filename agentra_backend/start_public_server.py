import uvicorn
from pyngrok import ngrok
import os
import sys

# 1. Start ngrok tunnel
try:
    # Open a HTTP tunnel on the default port 8000
    public_url = ngrok.connect(8000).public_url
    print(f"\n[NGROK] Public URL: {public_url}")
    print("[NGROK] COPY THIS URL: It will be used in the Flutter app.\n")
    
    # Save URL to a file for the agent to read
    with open("public_url.txt", "w") as f:
        f.write(public_url)
except Exception as e:
    print(f"Error starting ngrok: {e}")
    sys.exit(1)

# 2. Start FastAPI server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
