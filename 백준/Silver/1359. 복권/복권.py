from itertools import combinations

N, M, K = map(int, input().split())
arr = list(combinations(range(N), M))
results = 0
for i in arr:
    cnt = 0
    for j in range(M):
        if i[j] < M:
            cnt += 1
    if cnt >= K:
        results += 1
print(results/len(arr))