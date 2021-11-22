import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


n,k=map(int,input().split())
p=[]
for i in range(n):
  p.append(sum(map(int,input().split())))
p_s=[10000]+sorted(p,reverse=True)
border=p_s[k]
for s in p:
  if s+300>=border:
    print('Yes')
  else:
    print('No')