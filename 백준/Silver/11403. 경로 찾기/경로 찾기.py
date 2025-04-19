import sys
input = sys.stdin.readline

N = int(input())
graphs = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graphs[j][i] and graphs[i][k]:
                graphs[j][k] = 1
                
for g in graphs:
    print(' '.join(map(str, g)))