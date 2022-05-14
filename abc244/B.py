import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

def check_vector() :
    return (now_bector+1)%4

def cal_point():
    vector = s_dict[now_bector]
    x = now_point[0] + vector[0]
    y = now_point[1] + vector[1]
    return [x,y]

now_bector = 0
now_point = [0,0]
s_dict = {
    0:[1,0],
    1:[0,-1],
    2:[-1,0],
    3:[0,1],
    }

n = int(input())
T = input()

for i in range(n) :
    if T[i] == "S":
        now_point = cal_point()
    elif T[i] == "R":
        now_bector = check_vector()

print(' '.join(map(str,now_point)))