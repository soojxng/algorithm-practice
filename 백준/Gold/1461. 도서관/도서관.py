import sys
input = sys.stdin.readline

n, m = map(int, input().split())
minus = []
plus = []
for x in map(int, input().split()):
    if x < 0:
        minus.append(-x)
    else:
        plus.append(x)

minus.sort()
plus.sort()
ans = -max(minus[-1] if minus else 0, plus[-1] if plus else 0)

for i in range(len(minus)-1, -1, -m):
    ans += 2*minus[i]
for i in range(len(plus)-1, -1, -m):
    ans += 2*plus[i]

print(ans)