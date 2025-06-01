import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    M = int(input())
    if M == 1:
        print(1)
        print(int(input()))
        continue
    A = [list(map(int, input().split())) for _ in range(M//10+1)]
    h1 = [-min(A[0][0], A[0][1])]
    h2 = [max(A[0][0], A[0][1])]
    B = [A[0][0]]
    for i in range(2, M):
        x = A[i//10][i%10]
        if x <= -h1[0]: heapq.heappush(h1, -x)
        else: heapq.heappush(h2, x)
        while len(h1) - len(h2) > 1:
            heapq.heappush(h2, -heapq.heappop(h1))
        while len(h1) - len(h2) < 0:
            heapq.heappush(h1, -heapq.heappop(h2))
        if i % 2 == 0:
            B.append(-h1[0])
    print(len(B))
    for i in range(len(B)):
        print(B[i], end=' ')
        if i % 10 == 9:
            print()
        