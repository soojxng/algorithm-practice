import sys
input = sys.stdin.readline

def cal(i):
    l = minimum
    r = n
    ans = 0
    while l <= r:
        mid = (l+r) // 2
    
        cnt = 0
        tmp = 0
        for j in range(i, i+m):
            tmp += rubbers[j]
            if tmp >= mid:
                cnt += 1
                tmp = 0

        if cnt < k:
            r = mid-1
        else:
            ans = mid
            l = mid+1
    return ans

n, m, k  = map(int, input().split())
x = [int(input()) for _ in range(m)]
rubbers = [x[i]-x[i-1] for i in range(1, m)]
rubbers.append(x[0] + n - x[-1])
minimum = min(rubbers)
rubbers += rubbers

ans = -1
if m >= k:
    for i in range(m):
        ans = max(ans, cal(i))

print(ans)