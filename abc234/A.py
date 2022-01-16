import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


def myFunction(t) :
    return (t**2)+(2*t)+3


t = int(input())

print(myFunction(myFunction(myFunction(t) + t) + myFunction(myFunction(t))))