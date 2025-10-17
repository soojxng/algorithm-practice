import sys
input = sys.stdin.readline

n = int(input())
length = len(str(n))
ans = -1
while len(str(n)) == length:
    n *= 2
    ans += 1
print(ans)