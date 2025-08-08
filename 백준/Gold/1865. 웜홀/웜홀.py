import sys
input = sys.stdin.readline
        
for tc in range(int(input())):
    n, m, w = map(int, input().split())
    graph = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))
        
    costs = [0] * (n+1)
    f = 0
    for i in range(n):
        for s, e, t in graph:
            if costs[e] > costs[s] + t:
                costs[e] = costs[s] + t
                if i == n-1:
                    f = 1
    print('YES' if f else 'NO')