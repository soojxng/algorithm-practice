import sys
input = sys.stdin.readline

def check(n):
    visited[n] = 1
    
    for c in computers[n]:
        if not visited[c]:
            check(c)

N = int(input())

computers = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)
        
check(1)

print(sum(visited)-1)