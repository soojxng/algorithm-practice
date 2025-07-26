import sys
input = sys.stdin.readline

bulbs = [0]
for b in input().rstrip():
    if b == 'Y':
        bulbs.append(1)
    else:
        bulbs.append(0)

cnt = 0
for i in range(1, len(bulbs)):
    if bulbs[i]:
        for j in range(i, len(bulbs), i):
            bulbs[j] = 0 if bulbs[j] else 1
        cnt += 1
print(-1 if sum(bulbs) != 0 else cnt)