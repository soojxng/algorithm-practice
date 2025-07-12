import sys
input = sys.stdin.readline

N = int(input())
SW = [i//2 for i in range(2, N+2)]
for i in range(0, N, 2):
    SW[i] = N
    N -= 1
print(*SW)