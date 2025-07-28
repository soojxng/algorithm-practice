import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def makeTree(n, p):
    for v in connect[n]:
        if v != p:
            child[n].append(v)
            makeTree(v, n)
            
def cal(n):
    for c in child[n]:
        cal(c)
        ans[n] += ans[c]
        
n, r, q = map(int, input().split())
connect = [[] for _ in range(n+1)]
child = [[] for _ in range(n+1)]
ans = [1]*(n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)
makeTree(r, -1)
cal(r)

for _ in range(q):
    print(ans[int(input())])