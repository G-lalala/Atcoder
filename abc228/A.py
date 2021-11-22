import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


S, T, X = map(int, input().split())
if S < T:
    if S <= X < T:
        print("Yes")
    else:
        print("No")
else:
    if X < T or S <= X:
        print("Yes")
    else:
        print("No")