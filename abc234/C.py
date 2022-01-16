import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

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

n = int(input())

str_ans = int2str(n,2)

print(str_ans.replace('1','2'))