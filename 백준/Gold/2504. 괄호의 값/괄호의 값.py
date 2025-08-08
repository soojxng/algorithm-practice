s = []
ans = 0
tmp = 1
f = 1
e = list(input().rstrip())
for i in range(len(e)):
    if f == 0:
        break
    if e[i] == '(':
        s.append(2)
        tmp *= 2
    elif e[i] == '[':
        s.append(3)
        tmp *= 3
    elif e[i] == ')':
        if not s or s.pop() != 2:
            f = 0
            break
        if e[i-1] == '(':
            ans += tmp
        tmp //= 2
    elif e[i] == ']':
        if not s or s.pop() != 3:
            f = 0
            break
        if e[i-1] == '[':
            ans += tmp
        tmp //= 3

print(0 if s or not f else ans)