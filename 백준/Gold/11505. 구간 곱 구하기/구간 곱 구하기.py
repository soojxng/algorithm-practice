import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

MOD = 1000000007

def makeST(v, s, e):
    if s == e:
        tree[v] = nums[s]
        return
    
    mid = (s+e) // 2
    makeST(2*v, s, mid)
    makeST(2*v+1, mid+1, e)
    tree[v] = (tree[2*v] * tree[2*v+1]) % MOD

def update(v, s, e, b, c):
    if b < s or e < b:
        return
    
    if s == e:
        tree[v] = c
    else:
        mid = (s+e) // 2
        update(2*v, s, mid, b, c)
        update(2*v+1, mid+1, e, b, c)
        tree[v] = (tree[2*v] * tree[2*v+1]) % MOD
    
def cal(v, s, e, b, c):
    if c < s or e < b:
        return 1
    if b <= s and e <= c:
        return tree[v]
    
    mid = (s+e) // 2
    return (cal(2*v, s, mid, b, c) * cal(2*v+1, mid+1, e, b, c)) % MOD

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree = [0] * (4*n)
makeST(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:  #b번째 수를 c로 업데이트
        update(1, 0, n-1, b-1, c)
        nums[b-1] = c
    else:   #a==2, b~c 구간곱 출력
        print(cal(1, 0, n-1, b-1, c-1))