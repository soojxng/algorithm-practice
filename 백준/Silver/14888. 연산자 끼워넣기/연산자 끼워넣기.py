def cal(i, tmp):
    if i == N:
        m[0] = max(tmp, m[0])
        m[1] = min(tmp, m[1])
        return
    for j in range(4):
        if opers[j] > 0:
            opers[j] -= 1
            if j == 0: cal(i+1, tmp+nums[i])
            elif j == 1: cal(i+1, tmp-nums[i])
            elif j == 2: cal(i+1, tmp * nums[i])
            elif j == 3: cal(i+1, tmp//nums[i] if tmp > 0 else -((-tmp)//nums[i]))            
            opers[j] += 1

N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
m = [-float('inf'), float('inf')]
cal(1, nums[0])

for k in m:
    print(k)
