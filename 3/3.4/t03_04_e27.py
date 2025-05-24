n = int(input())

def cyclic(n):
    bin_str = bin(n)[2:]
    max = n
    curr = bin_str
    for _ in range(len(bin_str)):
        curr = curr[1:] + curr[0]
        val = int(curr, 2)
        if val > max:
            max = val
    return max

print(cyclic(n))
