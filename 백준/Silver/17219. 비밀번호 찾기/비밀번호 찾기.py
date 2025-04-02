import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = dict()

for _ in range(N):
    url, pw = input().strip().split()
    d[url] = pw

for _ in range(M):
    print(d[input().strip()])