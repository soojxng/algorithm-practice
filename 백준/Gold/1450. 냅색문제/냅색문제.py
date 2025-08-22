import sys
input = sys.stdin.readline

def bs(x):
    l = 0
    r = len(right)-1
    ans = -1
    while l <= r:
        m = (l+r)//2
        if right[m] <= x:
            ans = m
            l = m+1
        else:
            r = m-1
    return ans+1

def cal(i, cnt, a, s):
    if i == len(a):
        s.append(cnt)
        return
    cal(i+1, cnt+a[i], a, s)
    cal(i+1, cnt, a, s)
            
n, c = map(int, input().split())
arr = list(map(int, input().split()))
left = []
right = []
cal(0, 0, arr[:n//2], left)
cal(0, 0, arr[n//2:], right)
left.sort()
right.sort()

ans = 0
for l in left:
    if l > c:
        break
    ans = ans + bs(c-l)

print(ans)