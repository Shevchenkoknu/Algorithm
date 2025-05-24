def brackets(sequence):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return "no"
            stack.pop()

    return "yes" if not stack else "no"

sequence = input().strip()
print(brackets(sequence))
