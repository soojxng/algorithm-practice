import sys
input = sys.stdin.readline

def edit(s):
    a = s.count('0')

    if a * 2 > len(s):
        return '1' * len(s)
    elif a * 2 < len(s):
        return '0' * len(s)
    else:
        if s[0] == '0':
            return '1' + '0' * (len(s)-1)
        else:   # s[0] == '1'
            return '0' + '1' * (len(s)-1)

s = input().rstrip()
print(edit(s))