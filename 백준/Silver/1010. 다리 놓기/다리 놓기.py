import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    n, d = 1, 1
    for j in range(M, M-N, -1):
        n *= j
    for k in range(N, 0, -1):
        d *= k
    print(n // d)