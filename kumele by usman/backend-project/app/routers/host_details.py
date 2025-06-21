from fastapi import APIRouter, HTTPException
from typing import List
from app.models.host_details import HostDetails

router = APIRouter(prefix="/host-details", tags=["Host Details"])

# Simulated in-memory DB
host_db: List[HostDetails] = []

@router.post("/")
def create_host(host: HostDetails):
    for existing in host_db:
        if existing.id == host.id:
            raise HTTPException(status_code=400, detail="Host ID already exists")
    host_db.append(host)
    return {"message": "Host added", "host": host}

@router.get("/{host_id}")
def get_host(host_id: int):
    for host in host_db:
        if host.id == host_id:
            return host
    raise HTTPException(status_code=404, detail="Host not found")

@router.get("/")
def list_hosts():
    return {"hosts": host_db}
