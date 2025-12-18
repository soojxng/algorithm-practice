import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
hidden_layer = []
for i in range(m):
    tmp = list(map(int, input().split()))
    c = tmp[0]
    hidden_layer.append((tmp[1:c+1], tmp[c+1:2*c+1], tmp[-1]))
tmp = list(map(int, input().split()))
w2 = tmp[:-1]
b2 = tmp[-1]

tmp = [0]*n
for i in range(m):
    ww = w2[i]
    for p, w in zip(hidden_layer[i][0], hidden_layer[i][1]):
        tmp[p-1] += w*ww
    b2 += hidden_layer[i][2]*ww

for _ in range(q):
    a = list(map(int, input().split()))
    ans = b2
    for i in range(n):
        ans += tmp[i] * a[i]
    print(ans)