import sys
input = sys.stdin.readline

n = int(input())
visited = [0]*(n+1)
visited[1] = 1
k = 1
for i in range(2, n+1):
    if visited[i] != 0:
        continue
    k += 1
    for j in range(i, n+1, i):
        visited[j] = k

print(k)
print(*visited[1:])