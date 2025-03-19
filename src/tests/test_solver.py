# test_solver.py

import unittest
from solver import Solver


class TestSolver(unittest.TestCase):
    """Unit tests for the Solver class."""

    def setUp(self):
        """Set up a Solver instance before each test."""
        self.solver = Solver(a="a", b="b")

    def test_solve(self):
        """Test the solve method with valid inputs."""
        result = self.solver.solve(3, 4)
        self.assertEqual(result, 12, "solve(3, 4) should return 12")

    def test_solve_with_zero(self):
        """Test the solve method when one of the numbers is zero."""
        result = self.solver.solve(0, 5)
        self.assertEqual(result, 0, "solve(0, 5) should return 0")

    def test_solve_with_negative_numbers(self):
        """Test the solve method with negative numbers."""
        result = self.solver.solve(-3, 4)
        self.assertEqual(result, -12, "solve(-3, 4) should return -12")

        result = self.solver.solve(-3, -4)
        self.assertEqual(result, 12, "solve(-3, -4) should return 12")

    def test_solve_with_large_numbers(self):
        """Test the solve method with large numbers."""
        result = self.solver.solve(1000000, 1000000)
        self.assertEqual(
            result,
            1000000000000,
            "solve(1000000, 1000000) should return 1000000000000",
        )


if __name__ == "__main__":
    unittest.main()
