from fastapi import APIRouter
from app.models.chart_data import BarChartData

router = APIRouter(prefix="/bar-chart", tags=["Bar Chart"])

@router.get("/", response_model=BarChartData)
def get_bar_chart_data():
    # Example static data, replace with real logic later
    return BarChartData(
        labels=["Jan", "Feb", "Mar", "Apr"],
        values=[120, 150, 170, 130]
    )
