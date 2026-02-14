import sys
import heapq
input = sys.stdin.readline

l = int(input())
s = list(map(int, input().split()))
n = int(input())

h = []
for x in s:
    heapq.heappush(h, (0, x))
s.append(0)
s.sort()

for i in range(l):
    if s[i+1]-s[i]-1 <= n:
        for x in range(s[i]+1, s[i+1]):
            heapq.heappush(h, ((x-s[i])*(s[i+1]-x)-1, x))
    else:
        for j in range(1, n//2+1):
            x = s[i]+j
            heapq.heappush(h, ((x-s[i])*(s[i+1]-x)-1, x))
            x = s[i+1]-j
            heapq.heappush(h, ((x-s[i])*(s[i+1]-x)-1, x))
        if n % 2 == 1:
            x = s[i]+(n//2+1)
            heapq.heappush(h, ((x-s[i])*(s[i+1]-x)-1, x))

results = []
while h and len(results) < n:
    cnt, x = heapq.heappop(h)
    results.append(x)

x = s[-1]+1
while len(results) < n:
    results.append(x)
    x += 1

print(*results[:n])