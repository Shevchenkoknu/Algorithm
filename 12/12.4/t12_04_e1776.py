import sys

def train(n, order):
    cur = 1
    stack = []

    for wag in order:
        while cur <= n and (not stack or stack[-1] != wag):
            stack.append(cur)
            cur += 1
        if stack and stack[-1] == wag:
            stack.pop()
        else:
            return "No"
    return "Yes"

def main():
    data = sys.stdin.read().strip().split("\n")
    i = 0
    while i < len(data):
        n = int(data[i])
        if n == 0:
            break
        i += 1
        results = []
        while i < len(data) and data[i] != "0":
            order = list(map(int, data[i].split()))
            results.append(train(n, order))
            i += 1
        print("\n".join(results))
        print()
        i += 1

if __name__ == "__main__":
    main()
