def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть число.")


def read_uint(prompt: str) -> int:
    while True:
        try:
            v = int(input(prompt))
            if v >= 2:
                return v
            print("N має бути ≥ 2.")
        except ValueError:
            print("Помилка: введіть ціле число.")


def validate_variant() -> int:
    while True:
        v = input("Оберіть варіант (1: X1,X2,N; 2: X1,X2,delta): ").strip()
        if v in {"1", "2"}:
            return int(v)
        print("Допустимі значення: 1 або 2.")


def generate_grid(x1: float, x2: float, *, N: int = None, delta: float = None):
    if N is not None:
        delta = (x2 - x1) / (N - 1)
        return [x1 + i * delta for i in range(N)]
    else:
        xs = []
        x = x1
        while x <= x2 + 1e-12:
            xs.append(x)
            x += delta
        return xs


def find_sign_change_intervals(xs, fs):
    res = []
    for i in range(len(xs) - 1):
        if fs[i] == 0:
            res.append((xs[i], xs[i]))
        elif fs[i] * fs[i + 1] < 0:
            res.append((xs[i], xs[i + 1]))
    return res


def paginate_print(rows, page_size=20):
    for i, row in enumerate(rows, 1):
        print(row)
        if i % page_size == 0 and i != len(rows):
            input("Press Enter to continue...")
