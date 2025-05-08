import sys
input = sys.stdin.readline

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

m = 0
ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j: continue
        for k in range(5):
            if classes[i][k] == classes[j][k]:
                cnt += 1
                break
    if cnt > m:
        m = cnt
        ans = i+1
print(ans if ans else 1)