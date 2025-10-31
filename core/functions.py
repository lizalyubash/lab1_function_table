def f(x: float) -> float:
    return x ** 4 - 5 * x ** 3 - 0.25 * x ** 2 + 2


def deriv(f, x: float, h: float = 1e-5) -> float:
    """Числова похідна (центральна різниця)"""
    return (f(x + h) - f(x - h)) / (2 * h)
