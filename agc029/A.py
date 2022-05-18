import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


N = input()
ans = 0
num = 0

for i in range(len(N)) :
    if N[i] == "B" :
        num += 1
    else :
        ans += num
         
print(ans)
