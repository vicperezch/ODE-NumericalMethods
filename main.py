# Kimberly Ola
# Víctor Pérez
# Juan Solís

import numerical_methods as nm
import differential_equations as de
import numpy as np
import matplotlib.pyplot as plt

FINAL_X = 20
STEP = 0.01

def main():
    run = True
    x = np.linspace(0, FINAL_X, int(FINAL_X / STEP))

    while run:
        print("--- MÉTODOS NUMÉRICOS PARA ECUACIONES DIFERENCIALES ---")
        print("1. Primer orden - x")
        print("2. Segundo orden - Oscilador amortiguado")
        print("3. Sistema de ecuaciones - x y")
        print("4. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            pass

        elif option == "2":
            analytical_y = de.oscilator(x)
            t, numerical_y, y = nm.system_rk3(de.sust, de.y_second_order, t_0 = 0, x_0 = 1, y_0 = 0, t_f = FINAL_X, h = STEP)

            initialize_graph(
                x_label="Tiempo (s)", 
                y_label="Distancia (m)", 
                x=x, 
                numerical_y=numerical_y, 
                analytical_y=analytical_y
            )

        elif option == "3":
            pass

        elif option == "4":
            run = False

        print("")


# Crea y muestra la gráfica de las soluciones analítica y numérica
def initialize_graph(x_label: str, y_label: str, x: np.ndarray, numerical_y: np.ndarray, analytical_y: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))

    # Gráfica de ambas soluciones
    ax.plot(x, analytical_y, label="Solución analítica", color="blue")
    ax.plot(x, numerical_y, label="RK3", color="orange", linestyle="dashed")

    # Cuadrícula
    ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.6)

    # Títulos de los ejes
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    ax.axhline(0, color="black", linewidth=0.75)

    # Escala de los ejes
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=-1 * analytical_y.max())

    # Ocultar bordes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.legend()

    plt.show()


if __name__ == '__main__':
    main()
