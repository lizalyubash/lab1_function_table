from core.core import *
from core.functions import *


def main():
    print("=== Прототип 1: Мінімальний консольний інтерфейс ===")
    var = validate_variant()
    x1 = read_float("X1 = ")
    x2 = read_float("X2 = ")

    if var == 1:
        N = read_uint("N = ")
        xs = generate_grid(x1, x2, N=N)
    else:
        delta = read_float("delta = ")
        xs = generate_grid(x1, x2, delta=delta)

    fs = [f(x) for x in xs]
    print("№ | x | f(x)")
    for i, (x, fx) in enumerate(zip(xs, fs), 1):
        print(f"{i:3d} | {x: .6f} | {fx: .6f}")


if __name__ == "__main__":
    main()
