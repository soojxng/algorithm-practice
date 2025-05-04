import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for __ in range(2)]
    for i in range(1, n):
        tmp = max(stickers[0][i-2], stickers[1][i-2]) if i-2 >= 0 else 0
        stickers[0][i] += max(stickers[1][i-1], tmp)
        stickers[1][i] += max(stickers[0][i-1], tmp)
    print(max(stickers[0][-1], stickers[1][-1]))