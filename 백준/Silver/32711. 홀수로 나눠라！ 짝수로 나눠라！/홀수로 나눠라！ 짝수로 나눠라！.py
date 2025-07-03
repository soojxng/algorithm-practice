import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

tot = sum(A)
odd = sum(1 for a in A if a % 2 == 1)

if tot % 2 == 1: print(1)
else:
    if N == 1:
        print(0)
    elif odd >= 4:
        print(1)
    elif odd == 0:
        print(1)
    else:
        if A[0]%2 == A[-1]%2:
            print(0)
        else:
            print(1)