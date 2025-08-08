e = input().rstrip()
s = []

for a in e:
    if a in ('+', '-'):
        while s and s[-1] in ('+', '-', '*', '/'):
            print(s.pop(), end='')
        s.append(a)
    elif a in ('*', '/'):
        while s and s[-1] in ('*', '/'):
            print(s.pop(), end='')
        s.append(a)
    elif a == '(':
        s.append(a)
    elif a == ')':
        b = s.pop()
        while b != '(':
            print(b, end='')
            b = s.pop()
    else:
        print(a, end='')
while s:
    print(s.pop(), end='')