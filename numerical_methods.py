import numpy as np
import matplotlib.pyplot as plt
import typing

def graph(x: np.ndarray, y: np.ndarray):
    plt.plot(x, y)
    plt.show()


"""
Método de Runge-Kutta de tercer orden
f: función que representa la ecuación diferencial
y_0: valor inicial de y
x_0: valor inicial de x
x_f: valor final de x
h: paso
"""
def rk3(f, x_0: float, y_0: float, x_f: float, h: float) -> typing.Tuple[np.ndarray, np.ndarray]:
    x = np.arange(x_0, x_f, h)
    y = np.zeros(x.size)

    y[0] = y_0

    for i in range(1, x.size):
        x_i = x[i - 1]
        y_i = y[i - 1]

        k1 = f(x_i, y_i)
        k2 = f(x_i + h / 2, y_i + k1 * h / 2)
        k3 = f(x_i + h, y_i - k1 * h + 2 * k2 * h)

        y[i] = y[i - 1] + (k1 + 4 * k2 + k3) * h / 6
    
    return x, y
