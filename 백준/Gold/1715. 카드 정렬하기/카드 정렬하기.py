import sys
input = sys.stdin.readline
import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
cnt = 0
while len(cards) > 1:
    a, b = heapq.heappop(cards), heapq.heappop(cards)
    cnt += a+b
    heapq.heappush(cards, a+b)
print(cnt)