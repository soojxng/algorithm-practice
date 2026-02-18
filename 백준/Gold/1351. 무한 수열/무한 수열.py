import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def cal(x):
    if x not in d:
        d[x] = cal(x//p) + cal(x//q)
    return d[x]

n, p, q = map(int, input().split())
d = dict()
d[0] = 1
print(cal(n))