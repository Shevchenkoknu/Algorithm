n = int(input())
arr = list(map(int, input().split()))

def sort(arr, left, right):
    if left >= right:
        return

    pivot = arr[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    sort(arr, left, j)
    sort(arr, i, right)

sort(arr, 0, n - 1)
print(*arr)
