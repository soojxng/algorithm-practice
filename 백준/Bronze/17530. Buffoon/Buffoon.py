import sys
input = sys.stdin.readline

score = [int(input()) for _ in range(int(input()))]
print('S' if max(score) == score[0] else 'N')