import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
if a + b > n + 1:
    print(-1)
else:
    ans = []
    for i in range(1, a):
        ans.append(i)
    ans.append(max(a, b))
    for i in range(b-1, 0, -1):
        ans.append(i)
    
    if a + b < n + 1:
        print(ans[0], *(1 for _ in range(n+1-a-b)), *ans[1:])
    else:
        print(*ans)