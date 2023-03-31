from general import General
from latex import Latex

class Factors:
    # // Generate a random factor
    @staticmethod
    def random() -> str:
        return f"({General.rand_num()}x {General.rand_op()} {General.rand_num()})"
    
    # // Generate a task
    @staticmethod
    def new_task() -> str:
        return f"\\task ${Factors.random()}{Factors.random()}$" + Latex.newlines(5)
    
    # // Generate the tasks
    @staticmethod
    def generate_tasks(n: int) -> str:
        # // Generate the tasks
        tasks: str = "\n".join([Factors.new_task() for _ in range(n)])

        # // Return the tasks
        return Latex.start_tasks_env() + tasks + Latex.end_tasks_env()
    