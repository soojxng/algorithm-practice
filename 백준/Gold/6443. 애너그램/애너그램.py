import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bt():
    if len(s) == len(w):
        print(''.join(s))
        return
    
    for i in range(len(w)):
        if checked[i] or i > 0 and w[i] == w[i-1] and not checked[i-1]:
            continue
        checked[i] = 1
        s.append(w[i])
        bt()
        checked[i] = 0
        s.pop()

n = int(input())
for _ in range(n):
    w = list(input().rstrip())
    w.sort()
    s = []
    checked = [0]*len(w)
    bt()
