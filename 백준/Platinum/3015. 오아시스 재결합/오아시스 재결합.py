import sys
input = sys.stdin.readline

n = int(input())
s = []
ans = 0
tmp = 0
for _ in range(n):
    x = int(input())
    cnt = 1
    
    while s and s[-1][0] < x:
        ans += s[-1][1]
        s.pop()     
    if s and s[-1][0] == x:
        ans += s[-1][1]
        cnt = s[-1][1] + 1
        s.pop()
        if s: ans += 1
    else:
        if s: ans += 1
        
    s.append([x, cnt])
        
print(ans)