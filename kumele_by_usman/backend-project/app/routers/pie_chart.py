from fastapi import APIRouter
from app.models.chart_data import PieChartData

router = APIRouter(prefix="/pie-chart", tags=["Pie Chart"])

@router.get("/", response_model=PieChartData)
def get_pie_chart_data():
    # Example static data, replace with real logic later
    return PieChartData(data={"Completed": 70, "Pending": 20, "Failed": 10})
