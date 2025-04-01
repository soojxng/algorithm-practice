import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
b = []
ans = []

i, j = 0, 0
while i < n:
    i += 1
    b.append(i)
    ans.append('+')
    
    while b and b[-1] == a[j]:
        b.pop()
        ans.append('-')
        j += 1

print('NO' if b else '\n'.join(ans))
    