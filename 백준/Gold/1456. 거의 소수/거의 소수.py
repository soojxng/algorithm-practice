import sys
input = sys.stdin.readline

a, b = map(int, input().split())

checked = [1 for _ in range(int(b**0.5)+1)]
checked[0] = 0
checked[1] = 0
for i in range(2, int(len(checked)**0.5)+1):
    if not checked[i]:
        continue
    for j in range(i*i, len(checked), i):
        checked[j] = 0

cnt = 0
for i in range(2, int(b**0.5)+1):
    if checked[i]:
        x = i*i
        while x <= b:
            if x >= a:
                cnt += 1
            x *= i

print(cnt)