import sys
input = sys.stdin.readline

a, b = map(int, input().split())
length = min(b, 10**7)+1
checked = [1 for _ in range(length)]
checked[0] = 0
checked[1] = 0
for i in range(2, int(length**0.5)+1):
    if not checked[i]:
        continue
    for j in range(i*i, length, i):
        checked[j] = 0

for i in range(a, length):
    if checked[i] and str(i) == str(i)[::-1]:
        print(i)
print(-1)