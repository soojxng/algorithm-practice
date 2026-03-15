import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    max_q = []
    min_q = []
    k = int(input())
    visited = [0]*k
    for i in range(k):
        o, n = input().rstrip().split()
        if o == 'I':
            n = int(n)
            heapq.heappush(max_q, (-n, i))
            heapq.heappush(min_q, (n, i))
        elif n == '1':
            while max_q and visited[max_q[0][1]]:
                heapq.heappop(max_q)
            if max_q:
                visited[max_q[0][1]] = 1
                heapq.heappop(max_q)
        elif n == '-1':
            while min_q and visited[min_q[0][1]]:
                heapq.heappop(min_q)
            if min_q:
                visited[min_q[0][1]] = 1
                heapq.heappop(min_q)
    while max_q and visited[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and visited[min_q[0][1]]:
        heapq.heappop(min_q)
    if max_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print('EMPTY')