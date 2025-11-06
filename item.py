from fastapi import FastAPI, APIRouter



# Router
router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def get_items():
    return {"items": ["item1", "item2"]}

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
