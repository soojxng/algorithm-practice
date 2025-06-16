import sys
input = sys.stdin.readline     

def move(table, N, d):
    if d == 'up' or d == 'down':
        table = list(zip(*table))   
    if d == 'right' or d == 'down':
        table = [b[::-1] for b in table]
        
    tmp = [[x for x in b if x != 0] for b in table]
    ans = [[0]*N for _ in range(N)]
    for i in range(N):
        j = 0
        k = 0
        while j < len(tmp[i]):
            if j + 1 < len(tmp[i]) and tmp[i][j] == tmp[i][j+1]:
                ans[i][k] = tmp[i][j]*2
                j += 2
            else:
                ans[i][k] = tmp[i][j]
                j += 1
            k += 1
    
    if d == 'right' or d == 'down':
        ans = [b[::-1] for b in ans]
    if d == 'up' or d == 'down':
        ans = list(zip(*ans))
        
    return ans

for t in range(1, int(input())+1):
    N, DIR = input().rstrip().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(int(N))]
    ans = move(board, N, DIR)
    print(f'Case #{t}:')
    for a in ans:
        print(' '.join(map(str, a)))
                