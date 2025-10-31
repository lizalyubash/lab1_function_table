from core.core import *
from core.functions import *


def main():
    print("=== Прототип 5: Локалізований інтерфейс (укр.) ===")
    var = validate_variant()
    x1 = read_float("Початкове значення X1 = ")
    x2 = read_float("Кінцеве значення X2 = ")

    if var == 1:
        N = read_uint("Кількість точок N = ")
        xs = generate_grid(x1, x2, N=N)
    else:
        delta = read_float("Крок delta = ")
        xs = generate_grid(x1, x2, delta=delta)

    fs = [f(x) for x in xs]
    print("  № |      x      |     f(x)   ")
    print("-------------------------------")
    for i, (x, fx) in enumerate(zip(xs, fs), 1):
        print(f"{i:3d} | {x: .6f} | {fx: .6f}")


if __name__ == "__main__":
    main()
