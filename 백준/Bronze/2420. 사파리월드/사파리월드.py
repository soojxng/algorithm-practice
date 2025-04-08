N, M = map(int, input().split())

ans = N - M if N > M else M - N
print(ans)