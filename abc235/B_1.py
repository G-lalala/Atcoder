import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])



def checkMoveTower(now) :
    if now+1 < n and towers[now] < towers[now+1]:
        return True
    
    return False
 
 
n = int(input())
 
towers = list(map(int,input().split()))
 
now = 0
 
while checkMoveTower(now) :
    now += 1
 
print(towers[now])