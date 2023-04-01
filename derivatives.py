from general import General
from latex import Latex
from factors import Factors
import random

class Derivatives:
    # // Generate a random equation
    @staticmethod
    def random(n: int) -> str:
        # // Generate the numerator and denominator
        numerator: str = "".join([Factors.rand_factor(random.randint(1, 3)) for _ in range(n)])
        denominator: str = "".join([Factors.rand_factor(random.randint(1, 3)) for _ in range(n)])

        # // Return the equation
        return f"$\\frac{{d}}{{dx}}\\frac{{{numerator}}}{{{denominator}}}$" + Latex.newlines(5)
    
    # // Generate a task
    @staticmethod
    def new_task(n: int) -> str:
        return f"\\task {Derivatives.random(n)}"
    
    # // Generate the tasks
    @staticmethod
    def generate_tasks(n: int) -> str:
        # // Generate the tasks
        tasks: str = "\n".join([Derivatives.new_task(random.randint(1, 2)) for _ in range(n)])

        # // Return the tasks
        return Latex.start_tasks_env() + tasks + Latex.end_tasks_env()
    