from prettytable import PrettyTable

import numpy as np


class Model:

    def __init__(self):
        self.number_tests = 12
        self.x_max = 1
        self.x_min = -1
        self.x1 = []
        self.x2 = []
        self.signal = []
        self.response = []
        self.power = 0
        self.standart_deviation = 0
        self.func = lambda x1, x2: 1 + 4*x1 + 0.001 * x1 + 4 * x2 ** 2

    def add_couple(self, x1, x2):
        self.x1.append(x1)
        self.x2.append(x2)

    def compute_signal(self, i) -> float:
        x1 = self.x1[i]
        x2 = self.x2[i]
        signal = self.func(x1, x2)
        return signal

    def compute_standart_deviation(self) -> float:
        self.standart_deviation = self.power * 0.1

    def compute_power(self):
        avg_signal = [
            np.sum(self.signal) / len(self.signal)
            for i in range(len(self.signal))
        ]
        vec_avg_signal = np.array(avg_signal)
        power = np.vdot(self.signal - vec_avg_signal,
                        self.signal - vec_avg_signal) / len(self.signal)
        self.power = power

    def compute_response(self, error):
        self.response = self.signal + error


def generate_couple(x_min, x_max):
    x1 = np.random.uniform(x_min, x_max)
    x2 = np.random.uniform(x_min, x_max)
    return x1, x2


def generate_error(standart_deviation, number_tests) -> float:
    error = np.random.normal(0, standart_deviation, number_tests)
    return error


if __name__ == "__main__":

    model = Model()  # инициализируем модель

    for _ in range(model.number_tests):
        x1, x2 = generate_couple(model.x_min, model.x_max)
        model.add_couple(x1, x2)

    model.x1 = np.array(model.x1)
    model.x2 = np.array(model.x2)

    model.signal = np.array([
        model.compute_signal(i) for i in range(model.number_tests)
    ])

    model.compute_power()
    model.compute_standart_deviation()
    error = generate_error(model.standart_deviation, model.number_tests)
    model.compute_response(error)

    # Отрисовка таблицы
    table = PrettyTable()
    table.field_names = ["Num Test", "x1", "x2", "signal", "error", "response"]
    for i in range(model.number_tests):
        table.add_row([i+1, np.around(model.x1[i], 7),
                       np.around(model.x2[i], 7),
                       np.around(model.signal[i], 7),
                       np.around(error[i], 7),
                       np.around(model.response[i], 7)])
    print(table)
