import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    N = int(input())
    A = list(input().rstrip().split())
    ans = deque([A[0]])
    for i in range(1, N):
        if A[i] <= ans[0]:
            ans.appendleft(A[i])
        else:
            ans.append(A[i])
    print(''.join(ans))