import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    q = deque()
    q.append((A, ''))
    s = set([A])
    
    while 1:
        C, com = q.popleft()
        if C == B:
            print(com)
            break
        for t in [(C*2%10000, com+'D'), (C-1 if C > 0 else 9999, com+'S'), ((C%1000)*10 + (C//1000), com+'L'), ((C%10)*1000 + (C//10), com+'R')]:
            if t[0] not in s:
                s.add(t[0])
                q.append(t)
        