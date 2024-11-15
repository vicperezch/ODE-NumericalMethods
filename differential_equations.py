import numpy as np

# Ecuación de primer orden -
# 
def y_first_order(t: float, x: float, u: float) -> float:
    return 0


# Sustitución para ecuaciones de segundo orden 
# y' = u
def sust(t: float, x: float, u: float) -> float:
    return u


# Ecuación de segundo orden - Oscilador amortiguado
# y'' = 5cos(2t) - 4y - 9x
def y_second_order(t: float, x: float, y: float) -> float:
    return 5 * np.cos(2 * t) - 4 * y - 9 * x


# Solución analítica de la ecuación de segundo orden
# x(t) = (25cos(2t) + 40sin(2t)) / 89 + e^(-2t)(-25cos(5t) - 26sqrt(5)sin(5t)) / 89 + e^(-2t)(cos(5t) + 2sin(5t) / sqrt(5))
def oscilator(x: float) -> float:
    cos2x = np.cos(2 * x)
    sin2x = np.sin(2 * x)
    e2x = np.exp(-2 * x)
    cos5x = np.cos(np.sqrt(5) * x)
    sin5x = np.sin(np.sqrt(5) * x)

    return (25 * cos2x + 40 * sin2x) / 89 + e2x * (-25 * cos5x - 26 * np.sqrt(5) * sin5x) / 89 + e2x * (cos5x + 2 * sin5x / np.sqrt(5))


# Primera ecuación de un sistema
#
def x(t: float, x: float, y: float) -> float:
    return 0


# Segunda ecuación de un sistema
#
def y(t: float, x: float, y: float) -> float:
    return 0