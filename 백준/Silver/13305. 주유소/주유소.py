N = int(input())
dis = list(map(int, input().split()))
costs = list(map(int, input().split()))

minimum = float('inf')
cnt = 0

for i in range(N-1):
    if costs[i] < minimum:
        minimum = costs[i]
    cnt += minimum * dis[i]
    
print(cnt)