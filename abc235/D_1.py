import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])


a,n = map(int,input().split())

def changeHeadHip(number) :
    number = str(number)
    body = number[1:]
    head = number[0]
    return int(body+head)

def divideA(number) :
    return number/a

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


ans = 0

now_query = [n]

while len(now_query) != 0 :
    next_query = []

    for i in now_query :
        if divideA(i) == 1:
            print(ans + 1)
            exit()
        
        if is_integer_num(divideA(i)) :
            next_query.append(int(divideA(i)))

        snake_num = changeHeadHip(i)
        if snake_num >= 10 and snake_num%10 != 0 :
            next_query.append(snake_num)
    
    now_query = next_query
    ans += 1

print(-1)
