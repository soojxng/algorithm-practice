import sys
input = sys.stdin.readline

n = int(input())
dalls = list(map(int, input().split()))
dalls.sort()

counts = [0]*(max(dalls)+2)
for d in dalls:
    counts[d] += 1

ans = 0
for i in range(n):
    x = dalls[i]
    if not counts[x]:
        continue
    counts[x] -= 1
    
    ox = x
    while 1:
        x += 1
        if counts[x]:
            counts[x] -= 1
        else:
            ans += (x-ox) * (x-1)
            break

print(ans)