import sys
input = sys.stdin.readline

n, x, r, p, k = map(int, input().split())
regeneration = [1 if x == '1' else 0 for x in input().rstrip()]
r_s, p_s = 0, 0
ans = 0
damage = [((n-i)*p + (n-i)*r if regeneration[i] else (n-i)*p, i) for i in range(n)]
damage.sort(reverse=1)
s = set(damage[i][1] for i in range(k))
    
for i in range(n):
    if i in s:
        p_s += 1
    elif regeneration[i]:
        r_s += 1
            
    ans += x + (p*p_s) - (r*r_s)
    
print(ans)