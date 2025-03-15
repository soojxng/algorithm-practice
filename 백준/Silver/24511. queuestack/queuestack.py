import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

q = [B[i] for i in range(N-1, -1, -1) if A[i] == 0] + C

print(' '.join(map(str, q[:M])))

        
    