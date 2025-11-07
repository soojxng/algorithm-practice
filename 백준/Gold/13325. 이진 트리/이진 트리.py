import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def cal(v):
    if v*2 >= len(edges):
        return 0
    
    l = cal(v*2) + edges[v*2]
    r = cal(v*2+1) + edges[v*2+1]

    ans[0] += abs(l-r)

    return max(l, r)


k = int(input())
edges = [0, 0]+list(map(int, input().split()))
ans = [sum(edges)]

cal(1)
print(ans[0])