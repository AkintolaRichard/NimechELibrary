def eventEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "description": item["description"],
        "date": item["date"],
        "time": item["time"],
        "location": item["location"],
        "image_link": item["image_link"]
        }

def eventsEntity(entity) -> list:
    return [eventEntity(item) for item in entity]
