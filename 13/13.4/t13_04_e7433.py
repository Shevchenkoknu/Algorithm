A_input = input().strip()
P_input = input().strip()

def convert(A_str, P_str):
    A = int(A_str)
    P = int(P_str)

    if P <= 1:
        return
    if A == 0:
        return "0"

    stack = []

    while A > 0:
        remainder = A % P
        stack.append(remainder)
        A //= P
    result = []
    
    while stack:
        digit = stack.pop()
        if digit < 10:
            result.append(str(digit))
        else:
            result.append(f"[{digit}]")

    return ''.join(result)

print(convert(A_input, P_input))


