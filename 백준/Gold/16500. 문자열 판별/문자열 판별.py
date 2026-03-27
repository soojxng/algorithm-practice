import sys
input = sys.stdin.readline
    
s = input().rstrip()
n = int(input())
a = list(input().rstrip() for _ in range(n))
dp = [0]*(len(s)+1)
dp[0] = 1

for i in range(len(s)):
    if not dp[i]:
        continue

    for w in a:
        if i+len(w) <= len(s) and s[i:i+len(w)] == w:
            dp[i+len(w)] = 1

print(dp[-1])