import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(n)]

single = set()
multi = 0
cnt = 0

for b in boxes:
    f = 0
    for i in range(m):
        if f == 0 and b[i]:
            f = i+1
        elif f and b[i]:
            multi += 1
            f = 0
            break
    if f:
        if f in single:
            cnt += 1
        else:
            single.add(f)

if multi:
    cnt += multi-1
elif cnt:
    cnt -= 1

print(cnt)