import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

import time

def check_test_func(s,group) :
    ans = []
    for i in s :
        if i in group :
            ans.append('a')

s = [ i for i in range(100) if i % 2 == 0]

list_t = [ i for i in range(10000000)]
set_t = [ i for i in range(10000000)]

start = time.time()
check_test_func(s,list_t)
elapsed_time = time.time() - start
print("{:.03} ms in {}".format(elapsed_time * 1000, 'list_t'))

start = time.time()
check_test_func(s,set_t)
elapsed_time = time.time() - start
print("{:.03} ms in {}".format(elapsed_time * 1000, 'set_t'))