n = int(input())

def permutations(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            for p in permutations(rest):
                yield [lst[i]] + p

def op(a, b, c, d):
    ops = ['+', '-', '*', '/']

    def apply_op(x, y, op):
        if op == '+': return x + y
        if op == '-': return x - y
        if op == '*': return x * y
        if op == '/': return x / y if y != 0 else None

    def expressions(nums):
        for op1 in ops:
            for op2 in ops:
                for op3 in ops:
                    x, y, z, w = nums
                    results = []

                    try:
                        r = apply_op(apply_op(apply_op(x, y, op1), z, op2), w, op3)
                        if r is not None: results.append(r)
                    except: pass

                    try:
                        r = apply_op(apply_op(x, apply_op(y, z, op2), op1), w, op3)
                        if r is not None: results.append(r)
                    except: pass

                    try:
                        r = apply_op(x, apply_op(apply_op(y, z, op2), w, op3), op1)
                        if r is not None: results.append(r)
                    except: pass

                    try:
                        r = apply_op(x, apply_op(y, apply_op(z, w, op3), op2), op1)
                        if r is not None: results.append(r)
                    except: pass

                    try:
                        r = apply_op(apply_op(x, y, op1), apply_op(z, w, op3), op2)
                        if r is not None: results.append(r)
                    except: pass

                    for val in results:
                        if abs(val - 24.0) < 1e-6:
                            return True
        return False

    for perm in permutations([a, b, c, d]):
        if expressions(perm):
            return True
    return False

for _ in range(n):
    a, b, c, d = map(int, input().split())
    print("YES" if op(a, b, c, d) else "NO")
