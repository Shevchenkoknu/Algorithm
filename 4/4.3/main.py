#1.3787967711687088
def solve():
    def f(x):
        return x ** 3 + x + 1

    l, r = 0.0, 10.0
    eps = 1e-7

    while r - l > eps:
        mid = (l + r) / 2
        if f(mid) > 5:
            r = mid
        else:
            l = mid

    print(f"{r}")

solve()
