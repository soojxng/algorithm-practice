import sys
input = sys.stdin.readline

n = int(input())
bridge = [[0]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    bridge[a][b] = 1
    bridge[b][a] = 1

if n == 2:
    print(0)
    print(1)
elif n <= 4:
    print(n*(n-1)//2-(n-1))
    print(1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if bridge[i][j] == 0:
                print(i, j)
else:
    print(n-1-sum(bridge[1]))
    print(2)
    for i in range(2, n+1):
        if bridge[1][i] == 0:
            print(1, i)