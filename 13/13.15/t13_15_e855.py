n = int(input())

def gen(n):
    def backtrack(expr, stack, open_count):
        if len(expr) == n:
            if not stack:
                print(expr)
            return

        if open_count < n // 2:
            backtrack(expr + '(', stack + ['('], open_count + 1)
            backtrack(expr + '[', stack + ['['], open_count + 1)

        if stack:
            if stack[-1] == '(':
                backtrack(expr + ')', stack[:-1], open_count)
            if stack[-1] == '[':
                backtrack(expr + ']', stack[:-1], open_count)

    backtrack('', [], 0)

if n % 2 != 0:
    pass
else:
    gen(n)
