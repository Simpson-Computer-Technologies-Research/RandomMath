from factors import Factors
from latex import Latex
from derivatives import Derivatives

if __name__ == '__main__':
    # // Add a new header
    data: str = Latex.header("Random Factors")

    # // Generate the factors tasks
    data += Factors.generate_tasks(26)

    # // Add a new header
    data += Latex.header("Random Derivatives")
    
    # // Generate the derivative tasks
    data += Derivatives.generate_tasks(26)

    # // Write the data to a file
    Latex.write("main.tex", data)
