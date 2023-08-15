n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input())
cnt = 0
for _ in range(m):
    if input() in s:
        cnt += 1
print(cnt)