import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        nums[i][j] += max(nums[i-1][j-1] if j > 0 else 0, nums[i-1][j] if j < i else 0)
        
print(max(nums[-1]))