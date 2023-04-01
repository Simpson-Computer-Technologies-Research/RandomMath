from random import randint
import random

class Equations:
    # // Get a random operator
    @staticmethod
    def rand_op() -> str:
        return random.choice(['+', '-'])
    
    # // Generate a random polynomial
    @staticmethod
    def polynomial(degree: int, brackets = False) -> str:
        # // Determine the power of the variable
        to_power = lambda p: f"x^{{{p}}}" if p > 1 else "x" if p == 1 else ""
        
        # // Random number and the degree range
        degree_range: range = range(degree - 1, -1, -1)

        # // Generate other variables beyond the first one
        other_variables: str = "".join([
            f" {Equations.rand_op()} {randint(2, 9)}" + to_power(i) for i in degree_range
        ])

        # // Build the equation
        equation: str = f"{randint(2, 9)}" + to_power(degree) + other_variables
        
        # // Return the equation with brackets
        if brackets:
            return Equations.add_brackets(equation, randint(1, 3))
        
        # // Return the equation
        return equation
    
    # // Generate a random equation with brackets
    @staticmethod
    def add_brackets(equation: str, bracket_power: int) -> str:
        # // Generate the power as a string
        bracket_power_str: str = f"^{{{bracket_power}}}" if bracket_power > 1 else ""

        # // Return the equation and power
        return f"({equation})" + bracket_power_str
