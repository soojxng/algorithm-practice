import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())

for b in map(int, input().split()):
    if b in A:
        print(1)
    else:
        print(0)