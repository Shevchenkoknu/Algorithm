n = int(input())
numbers = [int(input()) for _ in range(n)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] % 10 > arr[j + 1] % 10) or \
               (arr[j] % 10 == arr[j + 1] % 10 and arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sort(numbers)
print(*numbers)
