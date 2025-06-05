import sys
input = sys.stdin.readline

P = int(input())
N = int(input())
stones = [0]*101
for _ in range(N):
    p, d = input().rstrip().split()
    s, e = 1, int(p)
    if d == 'R':
        s, e = int(p)+1, 101
    for i in range(s, e):
        stones[i] += 1
cnt = [0, 0, 0]
for tmp in stones[1:]:
    cnt[tmp%3] += 1
for c in cnt:
    print("%.2f" % (P*c/100))