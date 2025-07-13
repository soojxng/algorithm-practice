import sys
input = sys.stdin.readline
    
A = input().strip()
B = input().strip()
dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
if dp[-1][-1] != 0:
    x, y = len(A), len(B)
    ans = []
    while x > 0 and y > 0:
        if A[x-1] ==  B[y-1]:
            ans.append(A[x-1])
            x -= 1
            y -= 1
        elif dp[x-1][y] > dp[x][y-1]:
            x -= 1
        else:
            y -=1
    print(''.join(reversed(ans)))