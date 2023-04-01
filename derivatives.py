from latex import Latex
from equations import Equations
import random

class Derivatives:
    # // Generate a random equation
    @staticmethod
    def product_quotient(p: int, q: int) -> str:
        # // Generate the numerator
        numerator: str = "".join([
            Equations.with_brackets(
                random.randint(1, 3), random.randint(1, 2)) for _ in range(p)
        ])

        # // Generate the denominator
        denominator: str = "".join([
            Equations.with_brackets(
                random.randint(1, 3), random.randint(1, 2)) for _ in range(q)
        ])

        # // Build the derivative fraction
        build_frac = lambda n, d: f"$\\frac{{d}}{{dx}}\\frac{{{n}}}{{{d}}}$"

        # // Return the equation
        return build_frac(numerator, denominator) + Latex.newlines(5)
    
    # // Generate the tasks
    @staticmethod
    def product_quotient_tasks(amount: int) -> str:
        # // Generate a new task
        new_task = lambda p, q: f"\\task {Derivatives.product_quotient(p, q)}"
    
        # // Generate the tasks
        tasks: str = "\n".join([
            new_task(random.randint(1, 2), random.randint(1, 2)) 
                for _ in range(amount)
        ])

        # // Return the tasks
        return Latex.start_tasks_env() + tasks + Latex.end_tasks_env()
    