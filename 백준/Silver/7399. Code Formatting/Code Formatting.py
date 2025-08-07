import sys

tab = '    '
program = sys.stdin.readlines()
cnt = 0
ans = []
tmp = ''
for line in program:
    for l in line:
        if l == '{':
            if cnt != 0:
                tmp += ' '
            tmp += '{'
            ans.append(tmp)
            cnt += 1
            tmp = tab*cnt
        elif l == ',':
            tmp += ', '
        elif l == '}':
            cnt -= 1
            tmp = tab*cnt
            tmp += '}'
        elif l == ';':
            tmp += ';'
            ans.append(tmp)
            tmp = tab*cnt
        elif l.isspace():
            continue
        else:
            tmp += l

for a in ans:
    print(a)
print(tmp, end='')