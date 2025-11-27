import sys
input = sys.stdin.readline
from collections import deque
import math

def bfs():
    q = deque()
    q.append((1, 0, 0))
    ret = 0

    while q:
        v, i, tmp = q.popleft()

        if (v, v*2) not in br and (v, v*2+1) not in br:
            i += t

        for nv in (v*2, v*2+1):
            if nv >= size or (v, nv) in br:
                ret = max(ret, tmp)
                continue

            if (v, nv) not in br:
                q.append((nv, i, tmp + u + i))

    return ret

def dfs(v):
    global x
    ret = 0
    for nv in (v*2, v*2+1):
        if nv < size and (v, nv) not in br:
            x = nv
            ret += 1 + dfs(nv)

    return ret

d, n, u, t = map(int, input().split())
size = 2**d
br = set()
for _ in range(n):
    s, e = map(int, input().split())
    br.add((s, e))

x = 1
twin = bfs()
pony = (dfs(1)*2-(int(math.log2(x))))*u
if twin < pony:
    print(":blob_twintail_aww:")
elif pony < twin:
    print(":blob_twintail_sad:")
else:
    print(":blob_twintail_thinking:")