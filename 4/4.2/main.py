import math

def solve(c):
    l = 0
    r = max(1.0, math.sqrt(c) + 10)
    eps = 1e-7

    while r - l > eps:
        mid = (l + r) / 2
        f_mid = mid * mid + math.sqrt(mid)

        if f_mid < c:
            l = mid
        else:
            r = mid

    return l

def main():
    c = float(input())
    x = solve(c)
    print(f"{x:.10f}")

if __name__ == "__main__":
    main()
