N, M = map(int, input().split())
trees = list(map(int, input().split()))
s = 0
e = max(trees)
h = 0

while s <= e:
    m = (s + e)//2
    tmp = sum((t - m) if t - m > 0 else 0 for t in trees)
    if tmp >= M:
        h = m
        s = m+1
    else:
        e = m-1
        
print(h)