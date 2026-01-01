import sys
input = sys.stdin.readline

def cal(val):
    if val in s:
        return
    
    x = int(val**0.5)
    if x * x != val:
        x += 1

    y = x * x - val

    cal(x)
    cal(y)

    ans.append((x, y))
    s.add(val)

n = int(input())
s = {0, 1, 2}
ans = []
cal(n)
for x, y in ans:
    print(x, y)