import sys
from collections import deque

N = int(sys.stdin.readline())
dic = dict(zip(range(1, N+1), list(map(int, sys.stdin.readline().split()))))
dq = deque([x for x in range(1, N+1)])
answer = []
for _ in range(N):
    answer.append(dq[0])
    tmp = dic[dq.popleft()]
    dq.rotate(-(tmp - 1 if tmp > 0 else tmp))
    
print(' '.join(map(str, answer)))