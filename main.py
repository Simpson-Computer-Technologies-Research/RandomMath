from equations import Equations
from latex import Latex
from derivatives import Derivatives

if __name__ == '__main__':
    # // Add a new header
    data: str = Latex.header("Random Equations")

    # // Generate the random equations
    data += Equations.with_brackets_tasks(26)

    # // Add a new header
    data += Latex.header("Random Derivatives")
    
    # // Generate the random derivatives
    data += Derivatives.product_quotient_tasks(26)

    # // Write the data to a file
    Latex.write("main.tex", data)
