# worker.py

import asyncio
from solver import Solver


async def async_solve(solver: Solver, x: int, y: int):
    """
    Asynchronously solve a problem using the Solver class.
    """
    result = await asyncio.to_thread(solver.solve, x, y)
    print(f"Async result: {result}")


solver_instance = Solver(a="a", b="b")
asyncio.run(async_solve(solver_instance, 1, 2))
