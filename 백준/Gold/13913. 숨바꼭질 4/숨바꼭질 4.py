from collections import deque

N, K = map(int, input().split())
visited = [None for _ in range(100001)]
ans = []
q = deque([N])
visited[N] = -1
while q:
    num = q.popleft()
    if num == K:
        while num != -1:
            ans.append(num)
            num = visited[num]
        break
    for d in [num*2, num-1, num+1]:
        if 0 <= d <= 100000 and visited[d] is None:
            visited[d] = num
            q.append(d)
print(len(ans)-1)
print(*reversed(ans))