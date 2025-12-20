import sys
input = sys.stdin.readline

def is_prime(x):    
    i = 2
    while i*i <= x:
        if x % i == 0:
            return 0
        i += 1
    return 1

def bt(x, size):
    if size == n:
        print(x)
        return
    
    for i in (1, 3, 7, 9):
        tmp = x * 10 + i
        if is_prime(tmp):
            bt(tmp, size+1)

n = int(input())
for x in (2, 3, 5, 7):
    bt(x, 1)