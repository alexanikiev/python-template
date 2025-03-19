# main.py

import logging
import time
from solver import Solver

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main(solver: Solver):
    """
    Main function for solving a sample problem using the Solver class.
    Includes logging, exception handling, and execution time measurement.
    """
    try:
        x, y = 1, 2
        logging.info(f"Calling solve method with x={x}, y={y}")

        # Start measuring time
        start_time = time.perf_counter()

        result = solver.solve(x, y)

        # Stop measuring time
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        logging.info(f"Computation successful. Result: {result}")
        logging.info(f"Time taken: {elapsed_time:.6f} seconds")
        print(f"Result: {result} (Time taken: {elapsed_time:.6f} seconds)")

    except KeyboardInterrupt:
        logging.warning("Process interrupted by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    solver_instance = Solver(a="a", b="b")
    main(solver_instance)
