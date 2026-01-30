import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = input().rstrip()

s = []
for i in range(n):
    while s and s[-1] < num[i] and k > 0:
        s.pop()
        k -= 1
    s.append(num[i])

print(''.join(s[:-k] if k > 0 else s))