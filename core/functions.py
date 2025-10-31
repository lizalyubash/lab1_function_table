def f(x: float) -> float:
    """TODO: реалізувати обчислення функції згідно варіанту"""
    pass


def deriv(f, x: float, h: float = 1e-5) -> float:
    """Числова похідна (центральна різниця)"""
    return (f(x + h) - f(x - h)) / (2 * h)
