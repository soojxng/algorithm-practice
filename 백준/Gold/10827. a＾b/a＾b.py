import sys
input = sys.stdin.readline

a, b = input().rstrip().split()
b = int(b)
i = a.find('.')
cnt = (len(a) - i - 1) * b
n = str(int(a[:i]+a[i+1:]) ** b)
if len(n) <= cnt:
    n = '0' * (cnt - len(n) + 1) + n
print(f'{n[:-cnt]}.{n[-cnt:]}')