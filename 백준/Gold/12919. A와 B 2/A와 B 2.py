import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def cal(t):
    ret = 0
    if s == ''.join(t):
        return 1
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        ret = max(ret, cal(t[:-1]))
    if t[0] == 'B':
        ret = max(ret, cal(t[1:][::-1]))

    return ret

print(cal(t))