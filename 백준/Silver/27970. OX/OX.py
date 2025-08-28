import sys
input = sys.stdin.readline

n = 10**9+7
s = input().rstrip()
x = 1
ans = 0
for a in s:
    if a == 'O':
        ans = (ans + x) % n
    x = (x * 2) % n
    
print(ans)