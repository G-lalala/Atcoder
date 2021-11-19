import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])



N = int(input())

string = input()

for i in range(N) :
    print(string)