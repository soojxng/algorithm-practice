import sys
import re
input = sys.stdin.readline

def push(x, n):
    if x in el:
        el[x] += n
    else:
        el[x] = n
    return n

def cal(i, f):
    tmp = ''
    n = 1
    total = 0
    for a in eq[i]:
        if a.isspace():
            continue
        elif a == '+':
            if tmp:
                total += push(tmp, n*f)
            n = 1
            tmp = ''
        elif a.isnumeric():
            if tmp:
                total += push(tmp, n*int(a)*f)
                tmp = ''
            else:
                n = int(a)
        else:
            if tmp:
                total += push(tmp, n*f)
            tmp = a
    if tmp:
        total += push(tmp, n*f)
    return total
        
case = 1
while 1:
    eq = input().rstrip().split('=')
    if eq[0] == '#':
        break
    eq = [re.findall(r'\d+|[A-Z][a-z]*|\+|=', e) for e in eq]
    el = dict()
    total = 0
    
    for i, f in ((0, 1), (1, -1)):
        total += cal(i, f)
        
    if total == 0:
        print(f'Equation {case} is balanced.')
    else:
        print(f'Equation {case} is unbalanced.')
        for e in sorted(el.keys()):
            if el[e] > 0:
                print(f"You have destroyed {abs(el[e])} {'atom' if el[e] == 1 else 'atoms'} of {e}.")
            if el[e] < 0:
                print(f"You have created {abs(el[e])} {'atom' if el[e] == -1 else 'atoms'} of {e}.")
        print()
    case += 1