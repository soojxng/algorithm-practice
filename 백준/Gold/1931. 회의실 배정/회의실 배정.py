import sys
input = sys.stdin.readline

N = int(input())
times = []
tmp = 0
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    times.append((b, a))

times.sort()

for b, a in times:
    if a >= tmp:
        tmp = b
        cnt += 1
            
print(cnt)