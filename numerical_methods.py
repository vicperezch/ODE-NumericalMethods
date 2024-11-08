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


"""
Método de Adams-Bashforth-Moulton
f: función que representa la ecuación diferencial
y_0: valor inicial de y
x_0: valor inicial de x
x_f: valor final de x
h: paso
"""
def abm(f, x_0: float, y_0: float, x_f: float, h: float):
    x = np.arange(x_0, x_f, h)
    y = np.zeros(x.size)

    np.put(y, [0, 1, 2, 3], (rk3(f, x_0, y_0, x_0 + 4 * h, h)[1]))

    for i in range(4, x.size):
        y_1 = f(x[i - 1], y[i - 1])
        y_2 = f(x[i - 2], y[i - 2])
        y_3 = f(x[i - 3], y[i - 3])
        y_4 = f(x[i - 4], y[i - 4])

        pred = y[i - 1] + (55 * y_1 - 59 * y_2 + 37 * y_3 - 9 * y_4) * h / 24
        corr = y[i - 1] + (9 * f(x[i], pred) + 19 * y_1 - 5 * y_2 + y_3) * h / 24

        y[i] = corr
    
    return x, y
