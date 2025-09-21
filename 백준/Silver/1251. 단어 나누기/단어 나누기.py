s = input().rstrip()
n = len(s)
ans = '~'

for i in range(1, n-1):
    for j in range(i+1, n):
        ans = min(s[:i][::-1]+s[i:j][::-1]+s[j:][::-1], ans)

print(ans)