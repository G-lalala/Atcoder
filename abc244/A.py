import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

n = input()
S = input()

print(S[-1])