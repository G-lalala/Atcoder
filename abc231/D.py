import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

n,m = map(int,input().split())

number_array = [[] for i in range(n)]

for i in range(m) :
    a,b = map(int,input().split())
    a_array = number_array[a-1]
    b_array = number_array[b-1]

    if len(a_array) >= 2 or len(b_array) >= 2 :
        print('No')
        exit()
    
    a_array.append(b-1)
    b_array.append(a-1)

print(number_array)
