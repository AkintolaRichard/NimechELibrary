def eventEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "description": item["description"],
        "date": item["date"],
        "venue": item["venue"]
        }

def eventsEntity(entity) -> list:
    return [eventEntity(item) for item in entity]
