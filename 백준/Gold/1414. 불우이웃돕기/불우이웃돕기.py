import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    parents[find(a)] = find(b)

n = int(input())
board = [input().rstrip() for _ in range(n)]
edges = []
parents = [i for i in range(n+1)]

tot = 0
A_val = ord('A')
a_val = ord('a')
for i in range(n):
    for j in range(n):
        if board[i][j] == '0':
            continue
        x = ord(board[i][j])
        if x >= a_val:
            x = x - a_val + 1
        elif x >= A_val:
            x = x - A_val + 27
        tot += x
        if i != j:
            edges.append((x, i, j))
edges.sort()

tmp = 0
cnt = 0
for x, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        tmp += x
print((tot - tmp) if cnt == n-1 else -1)