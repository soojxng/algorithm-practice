import sys
input = sys.stdin.readline

def cal(i, j):
    while i < j:
        if s[i] != s[j]:
            return 2
        i += 1
        j -= 1
    return 1

t = int(input())
for _ in range(t):
    s = input().rstrip()
    i, j = 0, len(s)-1
    ans = 0
    while i < j:
        if s[i] != s[j]:
            ans = min(cal(i+1, j), cal(i, j-1))
            break
        i += 1
        j -= 1
    print(ans)