import sys
input = sys.stdin.readline
        
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1, -1, -1):
    ans += xy[i][1]*xy[i-1][0] - xy[i][0]*xy[i-1][1]
    
print(abs(ans)/2)