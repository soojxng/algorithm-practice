import sys
input = sys.stdin.readline

def find(n, n2):
    for i in range(2, n2+1, 1):
        if n % i == 0:
            return -1
    return 0

t = int(input())

for _ in range(t):
    n = int(input())
    flag = -1
    if n == 0 or n == 1:
        print(2)
        continue
    while True:
        flag = find(n, int(n ** (1/2)))
        if flag == 0:
            print(n)
            break
        n += 1