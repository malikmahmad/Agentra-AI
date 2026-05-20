# Agentra AI - Autonomous Content-to-Action Agent
**Challenge 1: Autonomous Content-to-Action Agent (Insight → Action System)**

## Project Overview
Agentra AI is a high-performance, standalone mobile application designed for the #AISeekho 2026 Google Antigravity Hackathon. It transforms unstructured business reports, CSV data, and news feeds into meaningful insights and automated action simulations.

## Key Features
- **True Standalone Operation:** No laptop or local server required. The app executes all multi-agent logic directly on the device.
- **Agentic Workflow Orchestration:** Uses Google Antigravity (Gemini API) to manage 5 specialized agents in a reasoning chain.
- **Action Simulation:** Realistically simulates the execution of 5 prioritized actions, including mock CRM updates and system state changes.
- **Traceable Reasoning:** Provides a full "Agent Trace" logs for judges to see the thinking process of each agent.

## The Multi-Agent Pipeline
1. **Content Agent:** Extracts facts, numbers, and key signals from unstructured input.
2. **Insight Agent:** Detects patterns, contradictions, and non-trivial business insights.
3. **Impact Agent:** Analyzes operational and revenue consequences.
4. **Action Agent:** Generates exactly 5 prioritized, constraint-based actions.
5. **Simulation Agent:** Runs a mock execution, showing "Before vs After" states and execution logs.

## Tech Stack
- **Orchestration:** Google Antigravity (Gemini 1.5 Flash via Generative AI SDK)
- **Frontend:** Flutter (Premium Dark UI, Jakarta Sans Typography)
- **Animations:** Animate_do (Fade/Slide/Zoom interactions)
- **Deployment:** Standalone Android APK

## How to Run
1. Install `Agentra AI.apk` on any Android device.
2. Ensure you have an active internet connection.
3. Paste a sales report or news text into the "Unstructured Content" field.
4. Click "ACTIVATE AGENTS" to watch the neural orchestration in real-time.
5. Explore the "TRACE" and "SIMULATION" tabs to see the agentic decision-making.

---
*Created for #AISeekho 2026 Hackathon by Team Agentra.*
