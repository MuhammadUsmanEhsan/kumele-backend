from fastapi import APIRouter, HTTPException
from typing import List
from app.models.reward_popup import RewardPopup

router = APIRouter(prefix="/reward-popups", tags=["Reward Popups"])

db = {}
id_counter = 1

@router.get("/", response_model=List[RewardPopup])
def get_all_popups():
    return list(db.values())

@router.post("/", response_model=RewardPopup)
def create_popup(popup: RewardPopup):
    global id_counter
    popup.id = id_counter
    db[id_counter] = popup
    id_counter += 1
    return popup

@router.put("/{popup_id}", response_model=RewardPopup)
def update_popup(popup_id: int, popup: RewardPopup):
    if popup_id not in db:
        raise HTTPException(status_code=404, detail="Popup not found")
    popup.id = popup_id
    db[popup_id] = popup
    return popup

@router.delete("/{popup_id}")
def delete_popup(popup_id: int):
    if popup_id not in db:
        raise HTTPException(status_code=404, detail="Popup not found")
    del db[popup_id]
    return {"message": "Popup deleted"}
