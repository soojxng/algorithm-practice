import sys
input = sys.stdin.readline

def bt(i, tmp):
    if len(tmp) == n:
        print(*tmp)
        return
    
    if s:
        tmp.append(s.pop())
        bt(i, tmp)
        s.append(tmp.pop())
    if i <= n:
        s.append(i)
        bt(i+1, tmp)
        s.pop()

n = int(input())
s = []
bt(1, [])