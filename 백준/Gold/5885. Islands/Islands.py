import sys
input = sys.stdin.readline
 
n = int(input())
li = [(int(input()), i) for i in range(1, n+1)]
li.sort(reverse=1)
cnt = 0
checked = [0]*(n+2)
tmp = -1
max_val = 1

for h, i in li:
    if tmp != h:
        tmp = h
        max_val = max(max_val, cnt)

    checked[i] = 1
    if checked[i-1] and checked[i+1]:
        cnt -= 1
    elif not checked[i-1] and not checked[i+1]:
        cnt += 1

print(max_val)