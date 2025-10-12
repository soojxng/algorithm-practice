import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    a, b, c = input().rstrip().split()
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    dp[0][0] = 1

    for j in range(len(a)+1):
        for k in range(len(b)+1):
            if j > 0 and dp[j-1][k] and a[j-1] == c[j+k-1]:
                dp[j][k] = 1
            if k > 0 and dp[j][k-1] and b[k-1] == c[j+k-1]:
                dp[j][k] = 1

    print(f"Data set {i}: {'yes' if dp[-1][-1] else 'no'}")