# 🤖 Multi-Agent Productivity Assistant

## 🚀 Overview

This project is a **Multi-Agent AI System** that helps users manage tasks, schedules, and notes using multiple agents.

A **Main Agent (controller)** coordinates different specialized agents to handle user requests and execute workflows.

---

## 🧠 Architecture

The system follows a **multi-agent architecture**:

* 🧠 Main Agent (Controller)
* ✅ Task Agent (Task management)
* 📅 Calendar Agent (Scheduling)
* 📝 Notes Agent (Notes handling)
* 🤖 AI Agent (Fallback responses)

---

## ⚙️ Features

* ➕ Add tasks
* 📋 View tasks (stored in database)
* 📅 Schedule meetings/events
* 📝 Save notes
* 🔁 Multi-step workflow automation
* 🤖 AI fallback for unknown queries

---

## 🔄 Workflow Example

### Input:

plan my day

### Execution:

* Task Agent → adds task
* Calendar Agent → schedules event

### Output:

{
"task": "Task added successfully",
"event": "Event scheduled successfully",
"message": "Day planned successfully"
}

---

## 🛠️ Tech Stack

* Backend: FastAPI
* Language: Python
* Database: SQLite
* Architecture: Multi-Agent System

---

## 📁 Project Structure

multi-agent-ai/

main.py
main_agent.py
task_agent.py
calendar_agent.py
notes_agent.py
ai_agent.py
tasks.db

---

## ▶️ How to Run

### 1. Clone repository

git clone https://github.com/sinchanacs2005-cryptop/multi-agent-ai.git
cd multi-agent-ai

### 2. Create virtual environment

python -m venv venv
source venv/Scripts/activate

### 3. Install dependencies

pip install fastapi uvicorn

### 4. Run server

uvicorn main:app --reload

---

## 🌐 API Documentation

Open in browser:
http://127.0.0.1:8000/docs

---

## 🧪 Example Queries

* add task study AI
* show tasks
* schedule meeting tomorrow
* show schedule
* add note revise DSA
* plan my day
* hello

---

## 🏆 Key Highlights

* Multi-agent coordination
* API-based system
* Database integration
* Workflow automation
* Modular architecture

---

## 🔮 Future Improvements

* Integration with real calendar APIs
* LLM (OpenAI / Gemini) integration
* Web UI dashboard
* Cloud deployment

---

## 📌 Conclusion

This project demonstrates how **multiple AI agents collaborate** to manage tasks, schedules, and workflows effectively.

---

## 👨‍💻 Author

GitHub: https://github.com/sinchanacs2005-cryptop

