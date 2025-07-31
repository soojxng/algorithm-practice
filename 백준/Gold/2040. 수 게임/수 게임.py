import sys
input = sys.stdin.readline

n = int(input())
for _ in range(3):
    pref = list(map(int, input().split()))
    pref.append(0)
    pref = pref[::-1]
    dp = [0]*(n+2)
    for i in range(1, n+1):
        pref[i] += pref[i-1]
        
    for i in range(n, 0, -1):
        dp[i] = float('inf')
        for j in range(i, n+1):
            dp[i] = min(dp[i], pref[j] - pref[i-1] - dp[j+1])
        
    ans = dp[1]
    
    if ans < 0:
        print('A')
    elif ans > 0:
        print('B')
    else:
        print('D')