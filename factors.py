from general import General
from latex import Latex
import random

class Factors:
    # // Generate a random factor
    @staticmethod
    def rand_factor(n: int) -> str:
        function_power: int = random.randint(1, 3)

        # // Determine the power of the variable
        def power(i: int) -> str:
            if i == 1:
                return "x"
            if i > 1:
                return f"x^{{{i}}}"
            return ""

        # // Generate the factor
        other_variables: str = "".join([f" {General.rand_op()} {General.rand_num()}" + power(i) for i in range(n - 1, -1, -1)])
        factor: str = f"({General.rand_num()}" + power(n) + other_variables + ")"

        # // Generate the power
        power: str = "^{" + str(function_power) + "}" if function_power > 1 else ""

        # // Return the factor and power
        return factor + power
    
    
    # // Generate a task
    # // Generate a random equation
    @staticmethod
    def random(n: int) -> str:
        # // Generate the numerator and denominator
        equation: str = "".join([Factors.rand_factor(random.randint(1, 2)) for _ in range(n)])

        # // Return the equation
        return f"${equation}$" + Latex.newlines(5)
    
    # // Generate a task
    @staticmethod
    def new_task(n: int) -> str:
        return f"\\task {Factors.random(n)}"
    
    # // Generate the tasks
    @staticmethod
    def generate_tasks(n: int) -> str:
        # // Generate the tasks
        tasks: str = "\n".join([Factors.new_task(2) for _ in range(n)])

        # // Return the tasks
        return Latex.start_tasks_env() + tasks + Latex.end_tasks_env()
    