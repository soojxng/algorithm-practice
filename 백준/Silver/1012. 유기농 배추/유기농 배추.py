import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def search(x, y):
    if (x, y) not in s:
        return
    s.discard((x, y))
    if x != 0:
        search(x-1, y)
    if x != M-1:
        search(x+1, y)
    if y != 0:
        search(x, y-1)
    if y != N-1:
        search(x, y+1)

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    cnt = 0
    s = set(tuple(map(int, input().split())) for _ in range(K))
    while s:
        x, y = next(iter(s))
        search(x, y)
        cnt += 1
    print(cnt)