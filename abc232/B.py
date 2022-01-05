import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s = input()
t = input()

if s == t :
    print('Yes')
    exit()

first_s = alfabet.index(s[0])

ans_array_alfa = [alfabet[(first_s+i)%26] for i in range(len(alfabet))]

k = ans_array_alfa.index(t[0])

for i in range(len(s)) :
    move_k = alfabet[(alfabet.index(s[i])+k)%26]
    if t[i] != move_k :
        print('No')
        exit()

print('Yes')