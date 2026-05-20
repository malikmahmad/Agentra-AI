from google import genai
import os

# Using the provided API key
API_KEY = "AIzaSyCpmsS6oisFS6L8D8bM-fwvdFxrJJmBiIs"

client = genai.Client(api_key=API_KEY)

def call_gemini(prompt: str, system: str = "") -> str:
    """Core Antigravity call — Gemini via Google GenAI"""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                "system_instruction": system
            }
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
