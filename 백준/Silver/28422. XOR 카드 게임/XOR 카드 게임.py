N = int(input())
A = list(map(int, input().split()))
dp = [0]*N

def cal(i, j):
    tmp = A[i]
    for k in range(i+1, j):
        tmp ^= A[k]
    return bin(tmp)[2:].count('1')

if N == 1: print(0)
elif N == 2: print(cal(0, 2))
elif N == 3: print(cal(0, 3))
else:
    dp[1] = cal(0, 2)
    dp[2] = cal(0, 3)
    dp[3] = dp[1] + cal(2, 4)
    for i in range(4, N):
        dp[i] = max(dp[i-2] + cal(i-1, i+1), dp[i-3] + cal(i-2, i+1))
    print(dp[-1])