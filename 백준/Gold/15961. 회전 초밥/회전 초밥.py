import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
checked = [0 for _ in range(d+1)]
cnt = 0
max_val = 0
for i in range(n + k):
    if max_val == d:
        break

    if i >= k:
        checked[sushi[(i-k) % n]] -= 1
        if not checked[sushi[(i-k) % n]]:
            cnt -= 1

    if not checked[sushi[i%n]]:
        cnt += 1
    checked[sushi[i%n]] += 1

    max_val = max(max_val, (cnt + 1) if not checked[c] else cnt)
print(max_val)