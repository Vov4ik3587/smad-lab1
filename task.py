from typing import List, Tuple

import numpy as np


class Model:

    x_max = 1
    x_min = -1
    number_tests = 12

    def __init__(self):
        self.factors: List(Tuple) = []
        self.response = []
        self.func = lambda x1, x2: 1 + 4*x1 + 0.001 * x1 + 4 * x2 ** 2

    def add_couple(self, couple: Tuple[float, float]):
        self.factors.append(couple)

    def compute_y(self, factors: Tuple) -> float:
        x1 = factors[0]
        x2 = factors[1]
        response = self.func(x1, x2)
        return response


def generate_couple(x_min, x_max) -> Tuple:
    x1 = np.random.uniform(x_min, x_max)
    x2 = np.random.uniform(x_min, x_max)
    return (x1, x2)


if __name__ == "__main__":
    input_model = Model()  # инициализируем модель

    for _ in range(1, 12):
        couple = generate_couple(input_model.x_min, input_model.x_max)
        input_model.add_couple(couple)

    input_model.response = [
        input_model.compute_y(i) for i in input_model.factors
    ]

    for i in range(0, input_model.number_tests - 1):
        print("factors [x1,x2] \t\t response y")
        print(f"{np.around(input_model.factors[i], 7)}" +
              f" \t {input_model.response[i]:.7f}\n")
