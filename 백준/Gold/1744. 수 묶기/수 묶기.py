import sys
input = sys.stdin.readline

def cal(l):
    ans = 0
    for i in range(1, len(l), 2):
        ans += l[i-1] * l[i]
    if len(l) % 2 == 1:
        ans += l[-1]
    return ans

n = int(input())
p = []
m = []
ans = 0
for _ in range(n):
    x = int(input())
    if x <= 0:
        m.append(x)
    elif x == 1:
        ans += 1
    else:
        p.append(x)

p.sort(reverse=1)
m.sort()

ans += cal(m) + cal(p)
print(ans)