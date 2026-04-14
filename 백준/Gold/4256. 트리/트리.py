import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
def getPost(pl, pr, il, ir):
    if pl > pr:
        return
    
    i = ino_pos[pre[pl]]
    size = i - il
    
    getPost(pl+1, pl+size, il, i-1)
    getPost(pl+size+1, pr, i+1, ir)
    post.append(pre[pl])

t = int(input())
for _ in range(t):
    n = int(input())
    pre = list(map(int, input().split()))
    ino = list(map(int, input().split()))
    ino_pos = [0]*(n+1)
    for i in range(n):
        ino_pos[ino[i]] = i

    post = []
    getPost(0, n-1, 0, n-1)
    print(*post)