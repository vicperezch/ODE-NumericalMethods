import numpy as np

"""
Método de Runge-Kutta de tercer orden
f: función que representa la ecuación diferencial
y_0: valor inicial de y
x_0: valor inicial de x
x_f: valor final de x
h: paso
"""
def rk3(f, x_0: float, y_0: float, x_f: float, h: float):

    # Inicializar arrays para contener los valores de x, y
    x = np.arange(x_0, x_f, h)
    y = np.zeros(x.size)

    # Asignar la condición incial
    y[0] = y_0

    # Iteraciones del método
    for i in range(0, x.size - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + k1 * h / 2)
        k3 = f(x[i] + h, y[i] - k1 * h + 2 * k2 * h)

        y[i + 1] = y[i] + (k1 + 4 * k2 + k3) * h / 6
    
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

    # Inicializar arrays para contener los valores de x, y
    x = np.arange(x_0, x_f, h)
    y = np.zeros(x.size)

    # Utilizar RK3 para obtener los primeros 4 valores de y
    np.put(y, [0, 1, 2, 3], (rk3(f, x_0, y_0, x_0 + 4 * h, h)[1]))

    for i in range(4, x.size):
        # Obtener los valores de y anteriores
        y_1 = f(x[i - 1], y[i - 1])
        y_2 = f(x[i - 2], y[i - 2])
        y_3 = f(x[i - 3], y[i - 3])
        y_4 = f(x[i - 4], y[i - 4])

        # Predicción y corrección
        pred = y[i - 1] + (55 * y_1 - 59 * y_2 + 37 * y_3 - 9 * y_4) * h / 24
        corr = y[i - 1] + (9 * f(x[i], pred) + 19 * y_1 - 5 * y_2 + y_3) * h / 24

        y[i] = corr
    
    return x, y


"""
Método de Runge-Kutta de tercer orden adaptado a sistemas de 2x2
f1: función que representa la primera ecuación diferencial
f2: función que representa la segunda ecuación diferencial
t_0: valor inicial de t
x_0: valor inicial de x
y_0: valor inicial de y
t_f: valor final de t
h: paso
"""
def system_rk3(f1, f2, t_0: float, x_0: float, y_0: float, t_f: float, h: float):

    # Inicializar arrays para contener los valores de t, x, y
    t = np.arange(t_0, t_f, h)
    x = np.zeros(t.size)
    y = np.zeros(t.size)

    # Asignar las condiciones iniciales
    x[0] = x_0
    y[0] = y_0

    for i in range(1, x.size):
        t_i = t[i - 1]
        x_i = x[i - 1]
        y_i = y[i - 1]

        m1 = f1(t_i, x_i, y_i)
        k1 = f2(t_i, x_i, y_i)

        m2 = f1(t_i + h / 2, x_i + m1 * h / 2, y_i + k1 * h / 2)
        k2 = f2(t_i + h / 2, x_i + m1 * h / 2, y_i + k1 * h / 2)

        m3 = f1(t_i + h, x_i - m1 * h + 2 * m2 * h, y_i - k1 * h + 2 * k2 * h)
        k3 = f2(t_i + h, x_i - m1 * h + 2 * m2 * h, y_i - k1 * h + 2 * k2 * h)

        x[i] = x[i - 1] + (m1 + 4 * m2 + m3) * h / 6
        y[i] = y[i - 1] + (k1 + 4 * k2 + k3) * h / 6
    
    return t, x, y


"""
Método de Adams-Bashforth-Moulton adaptado a sistemas de 2x2
f1: función que representa la primera ecuación diferencial
f2: función que representa la segunda ecuación diferencial
t_0: valor inicial de t
x_0: valor inicial de x
y_0: valor inicial de y
t_f: valor final de t
h: paso
"""
def system_abm(f1, f2, t_0: float, x_0: float, y_0: float, t_f: float, h: float):
    
    # Inicializar arrays para contener los valores de x, y
    t = np.arange(t_0, t_f, h)
    x = np.zeros(t.size)
    y = np.zeros(t.size)

    # Utilizar RK3 para obtener los primeros 4 valores de x, y
    np.put(x, [0, 1, 2, 3], (system_rk3(f1, f2, t_0, x_0, y_0, t_0 + 4 * h, h)[1]))
    np.put(y, [0, 1, 2, 3], (system_rk3(f1, f2, t_0, x_0, y_0, t_0 + 4 * h, h)[2]))

    for i in range(4, x.size):
        # Obtener los valores de x anteriores
        x_1 = f1(t[i - 1], x[i - 1], y[i - 1])
        x_2 = f1(t[i - 2], x[i - 2], y[i - 2])
        x_3 = f1(t[i - 3], x[i - 3], y[i - 3])
        x_4 = f1(t[i - 4], x[i - 4], y[i - 4])

        # Obtener los valores de y anteriores
        y_1 = f2(t[i - 1], x[i - 1], y[i - 1])
        y_2 = f2(t[i - 2], x[i - 2], y[i - 2])
        y_3 = f2(t[i - 3], x[i - 3], y[i - 3])
        y_4 = f2(t[i - 4], x[i - 4], y[i - 4])

        # Predicción y corrección
        pred = x[i - 1] + (55 * x_1 - 59 * x_2 + 37 * x_3 - 9 * x_4) * h / 24
        corr = x[i - 1] + (9 * f1(t[i], pred, y[i - 1]) + 19 * x_1 - 5 * x_2 + x_3) * h / 24

        x[i] = corr

        pred = y[i - 1] + (55 * y_1 - 59 * y_2 + 37 * y_3 - 9 * y_4) * h / 24
        corr = y[i - 1] + (9 * f2(t[i], x[i], pred) + 19 * y_1 - 5 * y_2 + y_3) * h / 24

        y[i] = corr
    
    return t, x, y
