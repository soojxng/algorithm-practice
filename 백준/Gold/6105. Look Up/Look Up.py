import sys
input = sys.stdin.readline

n = int(input())
cows = [int(input()) for _ in range(n)]
s = []
ans = []
for i in range(n-1, -1, -1):
    while s and cows[s[-1]] <= cows[i]:
        s.pop()
    ans.append(s[-1]+1 if s else 0)
    s.append(i)

for a in reversed(ans):
    print(a)