n, k = map(int, input().split())

def permutations(n, k):
    prev = [False] * (n + 1)
    curr = []

    def back():
        if len(curr) == k:
            print(' '.join(map(str, curr)))
            return
        for i in range(1, n + 1):
            if not prev[i]:
                prev[i] = True
                curr.append(i)
                back()
                curr.pop()
                prev[i] = False
    back()

permutations(n, k)