import sys
input = sys.stdin.readline

eq = input().rstrip()
x = eq.find('x')
ans = []
if x != -1:
    n = int(eq[:x]) // 2
    if n == -1:
        ans.append('-')
    elif n != 1:
        ans.append(str(n))
    ans.append('xx')

    if x != len(eq)-1 and int(eq[x+1:]) != 0:
        if eq[x+1:] == '+1':
            ans.append('+')
        elif eq[x+1:] == '-1':
            ans.append('-')
        else:
            ans.append(eq[x+1:])
        ans.append('x')
elif int(eq) != 0:
    if eq == '-1':
        ans.append('-')
    elif int(eq) != 1:
        ans.append(eq)
    ans.append('x')
if eq == '0':
    ans.append('W')
else:
    ans.append('+W')

print(''.join(ans))