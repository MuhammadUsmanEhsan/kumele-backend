from fastapi import APIRouter
from app.models.chart_data import CalendarYearData

router = APIRouter(prefix="/calendar-year", tags=["Calendar Year"])

@router.get("/{year}", response_model=CalendarYearData)
def get_calendar_year_data(year: int):
    # Example static data, replace with real logic later
    return CalendarYearData(
        year=year,
        events={
            f"{year}-01-01": 5,
            f"{year}-02-14": 12,
            f"{year}-07-04": 8,
            f"{year}-12-25": 15
        }
    )
