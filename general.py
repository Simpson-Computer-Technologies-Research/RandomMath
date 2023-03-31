import random

class General:
    # // Random plus or minus
    @staticmethod
    def rand_op() -> str:
        return random.choice(["+", "-"])

    # // Generate a random number from -10 and 10
    @staticmethod
    def rand_num() -> int:
        return random.randint(2, 9)
    