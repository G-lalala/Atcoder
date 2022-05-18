import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


N = int(input())

ans = set()

for i in range(N) :
    number = int(input())
    if number in ans :
        ans.remove(number)
    else :
        ans.add(number)
        

print(len(ans))
