import sys
input = sys.stdin.readline

k = int(input())
for t in range(1, k+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s = int(input())
    print(f"Data Set {t}:")
    print(' '.join(map(str, sorted(set(graph[s])))))
    if t != k: print()
