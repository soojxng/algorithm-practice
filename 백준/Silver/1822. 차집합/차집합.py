import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = A - B
print(len(C))
if len(C):
    print(*sorted(list(C)))