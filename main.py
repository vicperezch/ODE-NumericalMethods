from numerical_methods import rk3, abm, graph

# Ecuación diferencial a resolver: y' = f(x, y)
def f(x: float, y: float) -> float:
    return y - x**2 + 1


def main():
    x1, y1 = rk3(f, 0, 0.5, 2, 0.01)
    x2, y2 = abm(f, 0, 0.5, 2, 0.01)
    graph(x1, y1)
    graph(x2, y2)


if __name__ == '__main__':
    main()