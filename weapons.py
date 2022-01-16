
## simple binary
def binary_search(sequence, target):
    length = len(sequence)
    low = 0
    high = length - 1
    while low <= high:
        middle = int((low + high) / 2)
        if target == sequence[middle]:
            return middle
        elif target < sequence[middle]:
            high = middle - 1
        elif target > sequence[middle]:
            low = middle + 1
    return low

# change prefics number
def int2str(n, base):
    if not 2 <= base <= 36:
        raise ValueError('base must be between 2 and 36')

    table = '0123456789abcdefghijklmnopqrstuvwxyz'
    buf = []
    while True:
        n, r = divmod(n, base)
        buf.append(table[r])
        if n == 0: break
    return ''.join(reversed(buf))