def handle_calendar(query):
    query = query.lower()

    if "show schedule" in query:
        return ["Meeting at 5 PM", "Study at 7 PM"]

    elif "schedule" in query or "meeting" in query:
        return "Event scheduled successfully"

    else:
        return "Calendar agent did not understand"