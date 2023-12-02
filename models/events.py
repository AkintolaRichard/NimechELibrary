from datetime import datetime, timedelta
from pydantic import BaseModel, validator
from enum import Enum

class Event(BaseModel):
    title: str
    description: str
    date: datetime
    venue: str

    @validator("date")
    def event_must_be_in_the_future(cls, value):
        if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
            raise ValueError("Event date must be timezone-aware")
        utc_offset = timedelta(hours=1)
        current_time = datetime.utcnow().replace(tzinfo=value.tzinfo) + utc_offset

        if value < current_time:
            print("It is in the past")
            raise ValueError("Event date must be in the future (UTC+1)")
        return value
