import sys
input = sys.stdin.readline

N = int(input())

size = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum((i - 1) // T + 1 for i in size if i != 0))
print(N // P, N % P)