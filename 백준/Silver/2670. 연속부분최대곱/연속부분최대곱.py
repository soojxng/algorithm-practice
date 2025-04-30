import sys
input = sys.stdin.readline

N = int(input())
nums = [float(input()) for _ in range(N)]
    
for i in range(1, N):
    nums[i] = max(nums[i], nums[i-1]*nums[i])
    
print('%0.3f' % max(nums))