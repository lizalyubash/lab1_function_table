import sys
from core.core import *
from core.functions import *


def main():
    print("=== Прототип 4: Виклик через аргументи CLI ===")
    if len(sys.argv) == 4:
        x1, x2, n = map(float, sys.argv[1:])
        xs = generate_grid(x1, x2, N=int(n))
    else:
        print("Використання: python main.py X1 X2 N")
        return

    fs = [f(x) for x in xs]
    for i, (x, fx) in enumerate(zip(xs, fs), 1):
        print(f"{i:3d} {x: .6f} {fx: .6f}")


if __name__ == "__main__":
    main()
