from numerical_methods import rk3, graph

# Ecuación diferencial a resolver: y' = f(x, y)
def f(x: float, y: float) -> float:
    return y - x**2 + 1


def main():
    x, y = rk3(f, 0, 0.5, 2, 0.01)
    graph(x, y)


if __name__ == '__main__':
    main()