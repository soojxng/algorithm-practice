import sys
input = sys.stdin.readline

def makeST(v, s, e):
    if s == e:
        tree[v][0] = nums[s]
        tree[v][1] = nums[s]
        return
    
    mid = (s+e) // 2
    makeST(2*v, s, mid)
    makeST(2*v+1, mid+1, e)
    tree[v][0] = min(tree[2*v][0], tree[2*v+1][0])
    tree[v][1] = max(tree[2*v][1], tree[2*v+1][1])
    
def cal(v, s, e, a, b):
    if b < s or e < a:
        return float('inf'), -float('inf')
    if a <= s and e <= b:
        return tree[v]
    
    mid = (s+e) // 2
    tmp = cal(2*v, s, mid, a, b) 
    tmp2 = cal(2*v+1, mid+1, e, a, b)
    return min(tmp[0], tmp2[0]), max(tmp[1], tmp2[1])

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree = [[0, 0] for _ in range(4*n)]
makeST(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    print(*cal(1, 0, n-1, a-1, b-1))