import sys
input = sys.stdin.readline     

def is_valid(x, y):
    for dx, dy in d:
        if checked[x+dx][y+dy] == 0:
            return 0
    return 1
    
def check(x, y, f):
    for dx, dy in d:
        checked[x+dx][y+dy] = f

def bt(cnt, total):
    global ans
    if cnt == 3:
        ans = min(ans, total)
        return
    for i in range(1, N-1):
        for j in range(1, N-1):
            if is_valid(i, j):
                check(i, j, 0)
                bt(cnt+1, total+costs[i][j])
                check(i, j, 1)                

N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]
costs = [g[:] for g in garden]
d = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
checked = [[1]*N for _ in range(N)]
for i in range(1, N-1):
    for j in range(1, N-1):
        costs[i][j] += garden[i-1][j]+garden[i+1][j]+garden[i][j-1]+garden[i][j+1]
ans = float('inf')

bt(0, 0)
print(ans)