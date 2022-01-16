import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


ans_dict = {}

n,q = map(int,input().split())

num_list = list(map(int,input().split()))

for i in range(n):
    if num_list[i] not in ans_dict :
        ans_dict[num_list[i]] = {}
    
    nums = len(ans_dict[num_list[i]])
    ans_dict[num_list[i]][nums + 1] = i+1

for i in range(q) :
    x,k = map(int,input().split())
    if x in ans_dict :
        if k in ans_dict[x] :
            print(ans_dict[x][k])
            continue
    
    print(-1)