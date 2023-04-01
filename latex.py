
class Latex:
    # // The latex file document header
    @staticmethod
    def doc_header() -> str:
        return "\\documentclass{article}\\title{Random Math Equations}\\author{Tristan Simpson}\\date{\\today}\\usepackage{tasks}\\usepackage{amssymb}\\begin{document}\\maketitle\n"

    # // The latex file footer
    @staticmethod
    def doc_footer() -> str:
        return "\n\end{document}"

    # // Start the tasks environment
    @staticmethod
    def start_tasks_env() -> str:
        return "\\begin{tasks}[label-align=left, label-offset={0mm}, label-width={5mm}, item-indent={5mm}, label-format={\\bfseries}, column-sep=15mm](2)\n"

    # // End the tasks environment
    @staticmethod
    def end_tasks_env() -> str:
        return "\n\\end{tasks}"
    
    # // Generate a header in latex
    @staticmethod
    def header(head: str) -> str:
        return f"\\section{{{head}}}\n"
    
    # // Generate a new line in latex
    @staticmethod
    def newlines(n: int) -> str:
        return "\\newline" * n

    # // Write the random equations to a file
    @staticmethod
    def write(filename: str, data: str) -> None:
        with open(filename, "w") as f:
            f.write(Latex.doc_header())
            f.write(data)
            f.write(Latex.doc_footer())
            f.close()

