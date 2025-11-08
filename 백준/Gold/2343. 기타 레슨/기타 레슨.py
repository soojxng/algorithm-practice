import sys
input = sys.stdin.readline

n, m  = map(int, input().split())
videos = list(map(int, input().split()))

l = max(videos)
r = sum(videos)

while l < r:
    mid = (l+r) // 2
    
    cnt = 1
    tmp = 0
    for v in videos:
        if tmp + v > mid:
            cnt += 1
            tmp = v
        else:
            tmp += v

    if cnt <= m:
        r = mid
    else:
        l = mid+1

print(l)