import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bt(x, cnt, mask):
    global ans
    if ans == n // 2:
        return
    if x == 1 or (mask & (1 << ej)):
        ans = max(ans, cnt)
        return
    
    if x % 2 == 0:
        cnt += 1
        for i in range(n):
            if (mask & (1 << i)) == 0 and i != ej:
                for j in range(n):
                    guilty[j] += r[i][j]
                bt(x-1, cnt, mask | (1 << i))
                for j in range(n):
                    guilty[j] -= r[i][j]
    else:
        max_val = -float('inf')
        j = -1
        for i in range(n):
            if (mask & (1 << i)) == 0 and guilty[i] > max_val:
                max_val = guilty[i]
                j = i
        bt(x-1, cnt, mask | (1 << j))

n = int(input())
guilty = list(map(int, input().split()))
r = [list(map(int, input().split())) for _ in range(n)]
ej = int(input())

ans = 0
bt(n, 0, 0)
print(ans)