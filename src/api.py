# api.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """Represents an item with a name and description."""

    name: str
    description: str


@app.get("/")
def read_root():
    """
    Root endpoint.

    Returns:
        dict: A simple greeting message.
    """
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Retrieve an item by its ID.

    Args:
        item_id (int): The unique identifier of the item.

    Returns:
        dict: A dictionary containing the item ID.
    """
    return {"item_id": item_id}


@app.post("/items/")
def create_item(item: Item):
    """
    Create a new item.

    Args:
        item (Item): An instance of the Item model.

    Returns:
        dict: A dictionary containing the created item.
    """
    return {"name": item.name, "description": item.description}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
