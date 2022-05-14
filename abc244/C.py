N = int(input())

num_array = [i+1 for i in range(((2*N)+1))]

while len(num_array) > 1 :
    print(num_array[0])
    num_array.remove(num_array[0])
    ans = int(input())
    num_array.remove(ans)

print(num_array[0])
input()
