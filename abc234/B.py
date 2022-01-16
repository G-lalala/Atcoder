import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


import math



def getDistance(x:list, y:list) :
    lenght = abs(x[0] - y[0])
    height = abs(x[1] - y[1])

    return math.sqrt((lenght**2) + (height**2))


n = int(input())

points = []
max_distance = 0

for i in range(n) :
    x = list(map(int,input().split()))
    for y in points :
        distance = getDistance(x,y)
        if max_distance < distance :
            max_distance = distance 
    points.append(x)

print(max_distance)
