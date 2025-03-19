# mydataclass.py

from dataclasses import dataclass


@dataclass
class MyDataClass:
    """
    MyDataClass is a simple data class that represents an entity.
    """

    x: int
    y: int


# Example usage:
# myclass = MyDataClass(1, 2)
# print(myclass)
