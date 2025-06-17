import sys
input = sys.stdin.readline     

for _ in range(int(input())):
    K = int(input())
    files = list(map(int, input().split()))
    arr = [0]*(K+1)
    for i in range(1, K+1):
        arr[i] = arr[i-1] + files[i-1]
        
    dp = [[float('inf')]*(K) for i in range(K+1)]
    for i in range(K):
        dp[i][i] = 0
    for i in range(2, K+1):
        for j in range(K-i+1):
            for k in range(j, j+i-1):
                dp[j][j+i-1] = min(dp[j][j+i-1], dp[j][k]+dp[k+1][j+i-1]+arr[j+i]-arr[j])
    print(dp[0][K-1])