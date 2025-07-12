import sys
input = sys.stdin.readline

P = []
N = int(input())
for a in range(1, N+1, 2):
    P.append(a)
for a in range(N if P[-1] != N else N-1, 0, -2):
    P.append(a)
print(*P)