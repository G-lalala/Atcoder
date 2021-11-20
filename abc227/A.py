import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

n,k,a = map(int,input().split())

member = [i + 1 for i in range(n)]

print(member[((a-1+k-1)%n)])