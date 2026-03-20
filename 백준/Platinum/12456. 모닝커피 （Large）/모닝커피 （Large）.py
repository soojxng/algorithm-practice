import sys
import heapq
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    coffee = []
    h = []
    for _ in range(n):
        ci, ti, si = map(int, input().split())
        coffee.append((ti, si, ci))
    coffee.append((0, 0, 0))
    coffee.sort(reverse=1)

    d = coffee[0][0]
    ans = 0
    for ti, si, ci in coffee:
        tmp = d - ti
        while tmp > 0 and h:
            sj, cj = heapq.heappop(h)
            if -cj <= tmp:
                ans += sj*cj
                tmp += cj
            else:
                heapq.heappush(h, (sj, cj+tmp))
                ans -= sj*tmp
                tmp = 0

        d = ti
        heapq.heappush(h, (-si, -ci))
    print(f'Case #{i}: {ans}')