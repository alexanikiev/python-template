# mybasemodelclass.py

from pydantic import BaseModel


class MyBaseModelClass(BaseModel):
    """
    MyBaseModelClass is a Pydantic model that represents an entity.
    """

    name: str
    description: str


# Example usage:
# myclass = MyBaseModelClass(name="a", description="b")
# print(myclass.dict())
# print(myclass.json())
