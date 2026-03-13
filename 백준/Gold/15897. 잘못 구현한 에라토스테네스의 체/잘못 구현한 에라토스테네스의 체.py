import sys
input = sys.stdin.readline

n = int(input())
m = n-1
cnt = n
i = 1
while i < n:
    j = m // (m // i)
    cnt += (m // i) * (j - i + 1)
    i = j + 1
print(cnt)