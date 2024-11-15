import numerical_methods as nm
import differential_equations as de
import numpy as np
import matplotlib.pyplot as plt


def main():
    x1 = np.linspace(0, 10, int(10 / 0.01))
    y1 = de.oscilator(x1)
    
    t, x, y2 = nm.system_abm(de.sust, de.y_second_order, t_0 = 0, x_0 = 1, y_0 = 0, t_f = 10, h = 0.01)

    initialize_graph(x_label="Tiempo (s)", y_label="Distancia (m)", title="Oscilador amortiguado", x=x1, numerical_y=x, analitical_y=y1)


def initialize_graph(x_label: str, y_label: str, title: str, x: np.ndarray, numerical_y: np.ndarray, analitical_y: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, analitical_y, label="Analítica", color="blue")
    ax.plot(x, numerical_y, label="Numérica", color="red", linestyle="dashed")

    ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.6)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    ax.axhline(0, color="black", linewidth=0.75)

    # Inicio del eje x en 0
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=-1 * analitical_y.max())

    ax.legend()

    plt.show()


if __name__ == '__main__':
    main()
