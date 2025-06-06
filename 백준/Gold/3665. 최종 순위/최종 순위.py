import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [[] for _ in range(n+1)]
    T = list(map(int, input().split()))
    indegree = [0]*(n+1)
    for i in range(0, n):
        indegree[T[i]] = i
        for j in range(i+1, n):
            arr[T[i]].append(T[j])
    tmp = indegree.copy()
    for k in range(int(input())):
        a, b = map(int, input().split())
        if tmp[a] < tmp[b]:
            a, b = b, a
        indegree[a] -= 1
        indegree[b] += 1
        arr[b].remove(a)
        arr[a].append(b)
    q = deque()
    ans = []
    f = 0
    for i in range(1, n+1):
        if indegree[i] == 0:
            indegree[i] = -1
            q.append(i)
    while q:
        if len(q) > 1:
            f = 1
            break
        v = q.popleft()
        ans.append(v)
        for a in arr[v]:
            indegree[a] -= 1
            if indegree[a] == 0:
                indegree[a] = -1
                q.append(a)
    if len(ans) < n:
        print('IMPOSSIBLE')
    elif f:
        print('?')
    else:
        print(' '.join(map(str, ans)))