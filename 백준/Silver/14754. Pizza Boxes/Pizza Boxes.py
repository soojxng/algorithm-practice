import sys
input = sys.stdin.readline     

n, m = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(n)]
checked = [-1]*n
total = sum(sum(b) for b in boxes)
for i in range(n):
    tmp = 0
    for j in range(m):
        if boxes[i][j] > tmp:
            tmp = boxes[i][j]
            checked[i] = j
    total -= tmp
for i in range(m):
    tmp = 0
    f = 1
    for j in range(n):
        if boxes[j][i] > tmp:
            tmp = boxes[j][i]
            if checked[j] == i:
                f = 0
            else: f = 1
    if f: total -= tmp
print(total)