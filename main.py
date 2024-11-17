# Kimberly Ola
# Víctor Pérez
# Juan Solís

import numerical_methods as nm
import differential_equations as de
import numpy as np
import matplotlib.pyplot as plt

FINAL_X = 5
STEP = 0.001

def main():
    run = True
    x = np.linspace(0, FINAL_X, int(FINAL_X / STEP) * 10)

    while run:
        print("--- MÉTODOS NUMÉRICOS PARA ECUACIONES DIFERENCIALES ---")
        print("1. Primer orden - x")
        print("2. Segundo orden - Oscilador amortiguado")
        print("3. Sistema de ecuaciones - Sistema de oferta y demanda")
        print("4. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            pass

        elif option == "2":
            analytical_y = de.oscilator(x)
            t, rk3_y, y = nm.system_rk3(de.sust, de.y_second_order, t_0 = 0, x_0 = 1, y_0 = 0, t_f = FINAL_X, h = STEP)
            t, abm_y, y = nm.system_abm(de.sust, de.y_second_order, t_0 = 0, x_0 = 1, y_0 = 0, t_f = FINAL_X, h = STEP)

            initialize_graph(
                x_label="Tiempo (s)", 
                y_label="Distancia (m)", 
                x=x, 
                t=t,
                rk3_y=rk3_y, 
                abm_y=abm_y,
                analytical_y=analytical_y
            )

        elif option == "3":
            analytical_x, analytical_y = de.system(x)
            t, rk3_x, rk3_y = nm.system_rk3(de.x, de.y, t_0 = 0, x_0 = 1, y_0 = -1, t_f = FINAL_X, h = STEP)
            t, abm_x, abm_y = nm.system_abm(de.x, de.y, t_0 = 0, x_0 = 1, y_0 = -1, t_f = FINAL_X, h = STEP)

            initialize_graph(
                x_label="Tiempo", 
                y_label="Demanda", 
                x=x, 
                t=t,
                rk3_y=rk3_x, 
                abm_y=abm_x,
                analytical_y=analytical_x
            )

            initialize_graph(
                x_label="Tiempo", 
                y_label="Oferta", 
                x=x, 
                t=t,
                rk3_y=rk3_y, 
                abm_y=abm_y,
                analytical_y=analytical_y
            )

        elif option == "4":
            run = False

        print("")


# Crea y muestra la gráfica de las soluciones analítica y numéricas
def initialize_graph(x_label: str, y_label: str, t: np.ndarray, x: np.ndarray, abm_y: np.ndarray, rk3_y: np.ndarray, analytical_y: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize=(8, 8))

    # Gráfica de las soluciones
    ax.plot(x, analytical_y, label="Solución analítica", color="black")
    ax.plot(t, rk3_y, label="RK3", color="orange", linestyle="dashed")
    ax.plot(t, abm_y, label="ABM", color="green", linestyle="dotted")

    # Cuadrícula
    ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.6)

    # Títulos de los ejes
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    ax.axhline(0, color="black", linewidth=0.75)

    # Escala de los ejes
    ax.set_xlim(left=0)

    # Ocultar bordes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.legend()

    plt.show()


if __name__ == '__main__':
    main()
