from pydantic import BaseModel

class Event(BaseModel):
    title: str
    description: str
    date: str
    time: str
    location: str
    image_link: str