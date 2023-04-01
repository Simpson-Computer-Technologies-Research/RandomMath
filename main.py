from equations import Equations
from latex import Latex
from derivatives import Derivatives

if __name__ == '__main__':
    # // Add random derivatives header
    data = Latex.header("Random Derivatives")
    
    # // Generate the random derivatives
    data += Derivatives.product_quotient_tasks(amount = 26)

    # // Write the data to a file
    Latex.write("main.tex", data)
