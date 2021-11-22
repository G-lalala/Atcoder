import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

from collections import defaultdict, deque
n, x = map(int, input().split())
a = list(map(lambda x:int(x)-1, input().split()))
flag = [0 for _ in range(n)]
now = x-1
flag[now] = True
while 1:
    if flag[a[now]]:
        break
    else:
        flag[a[now]] = True
        now = a[now]
print(sum(flag))