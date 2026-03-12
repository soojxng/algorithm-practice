import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
s = [[] for _ in range(4)]
for x in li:
    f = 0
    for i in range(4):
        if not s[i] or s[i][-1] < x:
            s[i].append(x)
            f = 1
            break
    if not f:
        break
print('YES' if f else 'NO')