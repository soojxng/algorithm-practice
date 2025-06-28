def cal(cnt, w):
    if cnt > n: return
    if dp[cnt][w]: return
    dp[cnt][w] = 1
    
    cal(cnt+1, w+weights[cnt-1])
    cal(cnt+1, abs(w-weights[cnt-1]))
    cal(cnt+1, w)

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
balls = list(map(int, input().split()))

dp = [[0]*(sum(weights)+1) for _ in range(n+1)]

cal(0, 0)

ans = []

for b in balls:
    if b > sum(weights): ans.append('N')
    elif dp[n][b]: ans.append('Y')
    else: ans.append('N')
    
print(*ans)