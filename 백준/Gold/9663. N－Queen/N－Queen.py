import sys
input = sys.stdin.readline

N = int(input())

col = set()
d_left = set()
d_right = set()
cnt = 0

def nqueens(i):
    global cnt
    
    if i == N:
        cnt += 1
        return
    
    for j in range(N):
        if j in col or (i - j) in d_left or (i + j) in d_right:
            continue
        
        col.add(j)
        d_left.add(i - j)
        d_right.add(i + j)
        
        nqueens(i + 1)
        
        col.remove(j)
        d_left.remove(i - j)
        d_right.remove(i + j)
                
nqueens(0)
print(cnt)