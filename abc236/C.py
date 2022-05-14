import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


n,m = map(int,input().split())

normal_train = list(input().split())
express_train = set(input().split())

for i in normal_train :
    ans = 'Yes' if i in express_train else 'No'
    print(ans)
