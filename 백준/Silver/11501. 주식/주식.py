import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    maximum = 0
    ans = 0
    for i in range(N-1, -1, -1):
        if A[i] > maximum:
            maximum = A[i]
        elif A[i] < maximum:
            ans += maximum - A[i]
    print(ans)