import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def findBth(v, s, e, b):
    tree[v] -= 1
    
    if s == e:
        return s
    
    mid = (s+e) // 2

    if tree[v*2] >= b:
        return findBth(v*2, s, mid, b)
    else:
        return findBth(v*2+1, mid+1, e, b - tree[v*2])

def update(v, s, e, b, c):
    if b < s or e < b:
        return
    
    tree[v] += c

    if s != e:
        mid = (s+e) // 2
        update(2*v, s, mid, b, c)
        update(2*v+1, mid+1, e, b, c)

n = int(input())
length = 1000000
tree = [0]*(4*length)

for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        print(findBth(1, 1, length, tmp[1]))
    else:
        update(1, 1, length, tmp[1], tmp[2])