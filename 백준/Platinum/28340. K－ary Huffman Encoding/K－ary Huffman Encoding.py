import sys
import heapq
#input = sys.stdin.readline

def dfs(r, cnt):
    if r < len(c):
        return c[r]*cnt
    
    ans = 0
    for v in arr[r]:
        ans += dfs(v, cnt + 1)    
    return ans

for t in range(int(input())):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    while (n - 1) % (k - 1) != 0:
        c.append(0)
        n += 1
    arr = [[] for i in range(n)]
    h = [[c[i], i] for i in range(n)]
    heapq.heapify(h)

    while len(h) > 1:
        x = 0
        tmp = []
        i = k
        while h and i > 0:
            w, j = heapq.heappop(h)
            x += w
            tmp.append(j)
            i -= 1
        arr.append(tmp.copy())
        heapq.heappush(h, [x, n])
        n += 1

    ans = dfs(n-1, 0)

    print(ans)