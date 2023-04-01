from latex import Latex
import random

class Equations:
    # // Get a random operator
    @staticmethod
    def rand_op() -> str:
        return random.choice(['+', '-'])
    
    # // Generate a random equation with brackets
    @staticmethod
    def with_brackets(bracket_power: int, degree: int) -> str:
        # // Determine the power of the variable
        to_power = lambda p: f"x^{{{p}}}" if p > 1 else "x" if p == 1 else ""
        
        # // Random number and the degree range
        rand_num = lambda: random.randint(2, 9)
        degree_range: range = range(degree - 1, -1, -1)

        # // Generate the equation
        other_variables: str = "".join([
            f" {Equations.rand_op()} {rand_num()}" + to_power(i) for i in degree_range
        ])
        equation: str = f"({rand_num()}" + to_power(degree) + other_variables + ")"

        # // Generate the power as a string
        bracket_power_str: str = f"^{{{bracket_power}}}" if bracket_power > 1 else ""

        # // Return the equation and power
        return equation + bracket_power_str
    
    # // Generate the tasks
    @staticmethod
    def with_brackets_tasks(amount: int) -> str:
        # // Generate a new task
        def new_task(n: int) -> str:
            equation: str = "".join([
                Equations.with_brackets(
                    random.randint(1, 3), random.randint(1, 2)) for _ in range(n)
            ])
            return f"\\task ${equation}$ {Latex.newlines(5)}"
    
        # // Generate the tasks
        tasks: str = "\n".join([new_task(2) for _ in range(amount)])

        # // Return the tasks
        return Latex.start_tasks_env() + tasks + Latex.end_tasks_env()
    