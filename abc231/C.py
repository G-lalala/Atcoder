import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

def binary_search(sequence, target):
    length = len(sequence)
    low = 0
    high = length - 1
    while low <= high:
        middle = int((low + high) / 2)
        if target == sequence[middle]:
            return middle
        elif target < sequence[middle]:
            high = middle - 1
        elif target > sequence[middle]:
            low = middle + 1
    return low



n,q=map(int,input().split())

height_list = [i for i in list(map(int,input().split()))]

height_list.sort()

all_nums = len(height_list)

for i in range(q) :
    x = int(input())
    sepa_index = binary_search(height_list, x)
    if all_nums == sepa_index:
        print(0)
        continue

    print(all_nums - sepa_index)


