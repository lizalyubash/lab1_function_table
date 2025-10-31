import math


def f(x: float) -> float:
    """Обчислення функції згідно з варіантом (через math.pow)"""
    return math.pow(x, 4) - 5 * math.pow(x, 3) - 0.25 * math.pow(x, 2) + 2


def deriv(f, x: float, h: float = 1e-5) -> float:
    """Числова похідна (центральна різниця)"""
    return (f(x + h) - f(x - h)) / (2 * h)
