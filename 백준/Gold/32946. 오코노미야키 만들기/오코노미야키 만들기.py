import sys
input = sys.stdin.readline

def ptom(p1, p2):
    cnt = float('inf')
    if p1 < p2 < m or m < p2 < p1:
        if abs(p2-m) % 2 == 0 and m not in (1, n) and abs(p1-m) % 2 == 1:
            cnt = mtos(m, m-1 if m < p2 else (m+1), abs(p1-m) + abs(p2-m)+1)
    elif abs(p1-m) % 2 == 1:
        cnt = mtos(m, p2, abs(p1-m))
    return cnt

def mtos(p1, p2, tmp):
    cnt = float('inf')
    if p1 < p2 <= s or s <= p2 < p1:
        if s not in (1, n):
            cnt = tmp + abs(p1-s) + abs(p2-s) + 1
    else:
        cnt = tmp + abs(p1-s)
    return cnt

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
s = int(input())

ans = min(ptom(p1, p2), ptom(p2, p1))
print(ans if ans < float('inf') else -1)