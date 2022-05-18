import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

N,K = map(int,input().split())

balls = list(map(int,input().split()))

balls_dict = {}

diff_num = len(set(balls)) - K
if diff_num <= 0 :
    print(0)
    exit()

for i in balls :
    if i not in balls_dict :
        balls_dict[i] = 0
    
    balls_dict[i] += 1
    
balls_dict = dict(sorted(balls_dict.items(), key=lambda x: x[1])
)
ans = 0
cnt = 0

for i in balls_dict :
    if cnt == diff_num :
        break;
    
    ans += balls_dict[i]
    cnt += 1

print(ans)
