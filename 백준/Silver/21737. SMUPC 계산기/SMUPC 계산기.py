import sys
import re
input = sys.stdin.readline

n = int(input())
e = input().rstrip()
a = re.findall(r'-?\d+|[A-Z]', e)
if a[-1] != 'C':
    a.pop()
    
if 'C' not in a:
    print('NO OUTPUT')
else:
    ans = []
    tmp = int(a[0])
    i = 1
    while i < len(a):
        if a[i] == 'C':
            ans.append(tmp)
        elif a[i] == 'S':
            tmp -= int(a[i+1])
        elif a[i] == 'M':
            tmp *= int(a[i+1])
        elif a[i] == 'U':
            x = int(a[i+1])
            if tmp < 0 and x > 0 or tmp > 0 and x < 0:
                tmp = -((-tmp)//x)
            else:
                tmp //= int(a[i+1])
        elif a[i] == 'P':
            tmp += int(a[i+1])
        if a[i] in ('S', 'M', 'U', 'P'):
            i += 1
        i += 1
    print(*ans)