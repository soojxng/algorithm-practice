import sys
input = sys.stdin.readline

def bt(x, tot, tmp):
    if x == n:
        if tot+tmp == 0:
            print(''.join(e))
        return
    
    for op in (' ', '+', '-'):
        e.append(op)
        e.append(str(x+1))
        if op == ' ':
            bt(x+1, tot, (tmp*10) + ((x+1) if tmp > 0 else -(x+1)))
        elif op == '+':
            bt(x+1, tot+tmp, x+1)
        elif op == '-':
            bt(x+1, tot+tmp, -x-1)
        e.pop()
        e.pop()     

t = int(input())
for i in range(t):
    n = int(input())
    e = ['1']
    bt(1, 0, 1)
    if i != t-1:
        print()