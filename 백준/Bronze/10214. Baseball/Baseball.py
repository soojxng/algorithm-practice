import sys
input = sys.stdin.readline

T = int(input())
Y = K = 0
for i in range(T):
    for j in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k
    print('Yonsei' if Y > K else('Korea' if K < Y else 'Draw'))
