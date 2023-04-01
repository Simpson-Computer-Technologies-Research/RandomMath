from latex import Latex
from equations import Equations
import random

class Derivatives:
    # // Generate a random equation
    @staticmethod
    def product_quotient(n_amount: int, d_amount: int) -> str:
        # // Generate the numerator
        numerator: str = "".join([
            Equations.with_brackets(
                bracket_power = random.randint(1, 3), 
                degree = random.randint(1, 2)
            ) for _ in range(n_amount)
        ])

        # // Generate the denominator
        denominator: str = "".join([
            Equations.with_brackets(
                bracket_power = random.randint(1, 3), 
                degree = random.randint(1, 2)
            ) for _ in range(d_amount)
        ])

        # // Build the derivative fraction
        frac = lambda n, d: f"$\\frac{{d}}{{dx}}\\frac{{{n}}}{{{d}}}$"

        # // Return the equation
        return frac(numerator, denominator) + Latex.newlines(5)
    
    # // Generate the tasks
    @staticmethod
    def product_quotient_tasks(amount: int) -> str:
        # // Generate a new task
        new_task = lambda n, d: f"\\task {Derivatives.product_quotient(n, d)}"
    
        # // Generate the tasks
        tasks: str = "\n".join([
            new_task(random.randint(1, 2), random.randint(1, 2)) 
                for _ in range(amount)
        ])

        # // Return the tasks
        return Latex.start_tasks_env() + tasks + Latex.end_tasks_env()
    