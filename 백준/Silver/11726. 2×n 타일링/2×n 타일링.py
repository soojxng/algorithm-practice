import sys
input = sys.stdin.readline

n = int(input())

a = [0, 1, 2] + [0]*(0 if n < 3 else n - 2)

for i in range(3, n + 1):
    a[i] = a[i-1] + a[i-2]

print(a[n] % 10007)
