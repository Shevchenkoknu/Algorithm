#0.9999999403953552

def solve():
    def f(x):
        return x ** 3 + 4 * x ** 2 + x - 6

    l, r = 0.0, 2.0
    eps = 1e-7

    while r - l > eps:
        mid = (l + r) / 2
        if f(mid) * f(l) <= 0:
            r = mid
        else:
            l = mid

    print(f"{l}")

solve()