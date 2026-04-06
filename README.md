# 🤖 Multi-Agent Productivity Assistant

## 🚀 Overview
This project is a multi-agent AI system that helps users manage tasks, schedules, and notes using multiple agents.

## 🧠 Architecture
- Main Agent (Controller)
- Task Agent
- Calendar Agent
- Notes Agent
- AI Response Agent

## ⚙️ Features
- Add and view tasks
- Schedule meetings
- Store notes
- Multi-step workflow (plan my day)
- AI fallback response

## 🔄 Workflow Example
User: "plan my day"

System:
- Adds task
- Schedules meeting
- Returns structured response

## 🛠️ Tech Stack
- FastAPI
- Python
- SQLite

## ▶️ How to Run

```bash
python -m venv venv
source venv/Scripts/activate
pip install fastapi uvicorn
uvicorn main:app --reload
