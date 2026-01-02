import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
s = int(input())

for i in range(n-1):
    if s == 0:
        break

    mi = i
    for j in range(i+1, min(n, i+s+1)):
        if nums[j] > nums[mi]:
            mi = j

    for j in range(mi, i, -1):
        nums[j], nums[j-1] = nums[j-1], nums[j]
        s -= 1

print(*nums)