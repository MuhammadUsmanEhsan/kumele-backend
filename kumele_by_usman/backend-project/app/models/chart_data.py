from pydantic import BaseModel
from typing import Dict

class PieChartData(BaseModel):
    data: Dict[str, float]  # e.g. {"Category1": 45.5, "Category2": 54.5}

class BarChartData(BaseModel):
    labels: list[str]       # e.g. ["Jan", "Feb", "Mar"]
    values: list[float]     # e.g. [100, 150, 130]

class CalendarYearData(BaseModel):
    year: int
    events: Dict[str, int]  # e.g. {"2025-01-01": 10, "2025-02-01": 15}
