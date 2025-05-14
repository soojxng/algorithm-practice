N, E = map(int, input().split())
D = sorted(list(map(int, input().split())))
cnt = 1
for i in range(1, N):
    if D[i] - D[i-1] >= E:
        cnt += 1
print(cnt)