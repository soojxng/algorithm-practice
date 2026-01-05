import sys
input = sys.stdin.readline

n = int(input())
A = [(int(input()), i) for i in range(n)]
A.sort()
ans = 0
for i in range(n):
    ans = max(ans, A[i][1] - i)

print(ans+1)