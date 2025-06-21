from pydantic import BaseModel
from datetime import datetime

class EventTime(BaseModel):
    event_id: int
    start_time: datetime
    end_time: datetime
