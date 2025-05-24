expression = input().strip()

def operator(c):
    return c in '+-*/'

def priority(op):
    if op in '+-':
        return 1
    elif op in '*/':
        return 2
    return 0

def fix(expression):
    stack = []

    for token in reversed(expression):
        if token.isalpha():
            stack.append((token, 3))
        else:
            left, left_prio = stack.pop()
            right, right_prio = stack.pop()
            cur_prio = priority(token)

            if left_prio < cur_prio:
                left = f'({left})'
            if right_prio < cur_prio or (right_prio == cur_prio and token in '-/'):
                right = f'({right})'

            new_expr = f'{left}{token}{right}'
            stack.append((new_expr, cur_prio))

    return stack[0][0]

print(fix(expression))
