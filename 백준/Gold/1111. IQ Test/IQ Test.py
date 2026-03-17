import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = set()
if n == 1:
    print('A')
else:
    for a in range(-200, 201):
        b = nums[1] - (nums[0] * a)
        i = 2
        f = 1
        while 1:
            if i == n:
                break
            elif nums[i-1]*a + b != nums[i]:
                f = 0
                break
            i += 1
        if f:
            ans.add(nums[-1]*a + b)
    if len(ans) == 0:
        print('B')
    elif len(ans) == 1:
        print(ans.pop())
    else:
        print('A')