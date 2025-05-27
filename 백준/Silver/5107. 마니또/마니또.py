import sys
from collections import deque
input = sys.stdin.readline

i = 1
while 1:
    n = int(input())
    if n == 0: break
    mnt = dict()

    for _ in range(n):
        tmp = list(input().strip().split())
        mnt[tmp[0]] = tmp[1]
    
    names = set(mnt.keys())

    q = deque()
    cnt = 0
    while names:
        q.append(names.pop())
        cnt += 1
        while q:
            x = q.popleft()
            if mnt[x] in names:
                names.remove(mnt[x])
                q.append(mnt[x])
            
    print(i, cnt)
    i += 1