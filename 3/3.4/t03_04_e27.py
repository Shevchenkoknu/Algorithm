n = int(input())

def cyclic(n):
    bin_str = bin(n)[2:]
    rotations = []
    curr = bin_str
    length = len(bin_str)

    for _ in range(length):
        val = int(curr, 2)
        rotations.append(val)
        curr = curr[1:] + curr[0]

    max_val = rotations[0]
    for val in rotations:
        if val > max_val:
            max_val = val
    return max_val

print(cyclic(n))
