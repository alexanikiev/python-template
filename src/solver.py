# solver.py

from pydantic import BaseModel


class Solver(BaseModel):
    """
    Solver is a class that represents a solver for a sample problem.
    """

    a: str
    b: str

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

    def error(self):
        """
        error is a public method that raises an exception.
        """
        raise ValueError("This is an error message.")


# Example usage:
# solver = Solver(a="a", b="b")
# result = solver.solve(1, 2)
# print(result)
