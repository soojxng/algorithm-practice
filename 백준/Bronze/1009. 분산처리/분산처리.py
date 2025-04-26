nums = [[i] for i in range(10)]
nums[0][0] = 10
for i in range(2, 10):
    while 1:
        tmp = (nums[i][-1]*i) % 10
        if tmp == i:
            break
        else: nums[i].append(tmp)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(nums[a%10][(b-1)%len(nums[a%10])])