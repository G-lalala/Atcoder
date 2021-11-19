import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

def sort_and_set(i) :
    L = list(map(int,input().split()))
    if L[0] == 1 :
        return str(L[1])
    
    seperate_array = L[1:]
    return 'A'.join(map(str,seperate_array))


N = int(input())

L_array = [sort_and_set(i) for i in range(N)]

print(len(set(L_array)))