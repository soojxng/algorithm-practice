import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    
else:
    p = n * 0.15
    p = int(p) if (p * 10) % 10 <5 else int(p) + 1

    diffi = [int(input()) for _ in range(n)]

    diffi.sort()

    avg = sum(diffi[p:n-p]) / (n - (p*2))
    print(int(avg) if (avg * 10) % 10 < 5 else int(avg) + 1)
    
