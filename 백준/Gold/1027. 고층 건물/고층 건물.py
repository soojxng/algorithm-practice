import sys
input = sys.stdin.readline

n = int(input())
buildings = list(map(int, input().split()))
results = [0]*n

for i in range(n-1):
    tmp = -float('inf')
    for j in range(i+1, n):
        a = (buildings[j] - buildings[i]) / (j-i)
        if tmp < a:
            results[i] += 1
            results[j] += 1
            tmp = a

print(max(results))