# mybehaviorclass.py


class MyBehaviorClass:

    """
    MyBehaviorClass is a simple class that represents an entity with behaviors.
    """

    def __init__(self):
        self.a = "a"
        self.b = "b"

    def _calculate(self, x: int, y: int) -> int:
        """
        _calculate is a private method that performs a calculation.
        """
        return x * y

    def solve(self, x: int, y: int) -> int:
        """ "
        solve is a public method that uses the _calculate method
        to perform a calculation.
        """
        return self._calculate(x, y)


# Example usage:
# myclass = MyBehaviorClass()
# result = myclass.solve(1, 2)
# print(result)
