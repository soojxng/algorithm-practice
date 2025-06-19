import sys
input = sys.stdin.readline     

X, Y = map(int, input().split())
for _ in range(int(input())):
    A = int(input())
    f = 0
    if X % A == 0 and (Y-2) % A == 0:
        f = 1
    elif (X-1) % A == 0 and (Y-1) % A == 0:
        f = 1
    elif (X-2) % A == 0 and Y % A == 0:
        f = 1
    elif X % A == 0 and (Y-1) % A == 0 and (X-2) % A == 0:
        f = 1
    elif Y % A == 0 and (X-1) % A == 0 and (Y-2) % A == 0:
        f = 1
    print('YES' if f else 'NO')