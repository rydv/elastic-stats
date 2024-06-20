from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
def read_items():
    return [{"item_id": "foo"}, {"item_id": "bar"}]

@router.get("/items/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id}