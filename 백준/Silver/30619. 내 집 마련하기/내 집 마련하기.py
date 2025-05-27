import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
for _ in range(M):
    L, R = map(int, input().split())
    cnt = L
    for a in A:
        if L <= a <= R and cnt <= R:
            print(cnt, end=' ')
            cnt += 1
        else:
            print(a, end=' ')
    print()
        