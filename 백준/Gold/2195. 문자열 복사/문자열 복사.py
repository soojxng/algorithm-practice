import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

cnt = 0
i = 0
while i < len(p):
    max_k = 0
    for j in range(len(s)):
        k = 0
        while i+k < len(p) and j+k < len(s) and p[i+k] == s[j+k]:
            k += 1
        max_k = max(k, max_k)
    i += max_k
    cnt += 1

print(cnt)