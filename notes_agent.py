def handle_notes(query):
    query = query.lower()

    if "note" in query:
        return "Note saved successfully"

    else:
        return "Notes agent did not understand"