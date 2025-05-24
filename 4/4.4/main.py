import math
#2.278862583637238
def solve():
    def f(x):
        return math.sin(x) - x / 3

    l, r = 1.6, 3.0
    eps = 1e-7

    while r - l > eps:
        mid = (l + r) / 2
        if f(mid) * f(l) <= 0:
            r = mid
        else:
            l = mid

    print(f"{l}")

solve()