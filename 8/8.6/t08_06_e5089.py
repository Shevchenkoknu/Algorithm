n = int(input())
words = [input().strip() for _ in range(n)]

def selection_sort(words):
    n = len(words)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if words[j] < words[min]:
                min = j
        words[i], words[min] = words[min], words[i]
selection_sort(words)

for word in words:
    print(word)
