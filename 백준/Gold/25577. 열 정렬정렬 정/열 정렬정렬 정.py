import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(enumerate(a), key=lambda x: x[1])

visited = [0]*n
ans = 0

for i in range(n):
    if visited[i]:
        continue

    j = i
    tmp = 0
    while not visited[j]:
        visited[j] = 1
        j = a_sorted[j][0]
        tmp += 1
    if tmp:
        ans += tmp-1

print(ans)