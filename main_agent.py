from task_agent import handle_task
from calendar_agent import handle_calendar
from notes_agent import handle_notes
from ai_agent import ai_response

def main_agent(query):
    query = query.lower()

    # 🔥 Multi-step workflow
    if "plan my day" in query:
        task = handle_task("add task study AI")
        event = handle_calendar("schedule meeting at 5 PM")

        return {
            "task": task,
            "event": event,
            "message": "Day planned successfully"
        }

    # Task agent
    elif "task" in query:
        return handle_task(query)

    # Calendar agent
    elif "schedule" in query or "meeting" in query:
        return handle_calendar(query)

    # Notes agent ✅
    elif "note" in query:
        return handle_notes(query)

    # AI fallback ✅
    else:
        return ai_response(query)