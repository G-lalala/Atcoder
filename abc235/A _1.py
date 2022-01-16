import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

a = input()

print(a)

ans = 0

for i in range(3) :
  ans += (int(a[0])*100)+(int(a[0])*10)+(int(a[0])*1)

print(ans)