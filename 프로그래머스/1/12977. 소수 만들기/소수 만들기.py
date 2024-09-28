MAX_NUM = 3001
def solution(nums):
    answer = 0
    prime_list = [1 for _ in range(MAX_NUM)]
    prime_list[0] = 0
    prime_list[1] = 0
    
    for i in range(2, MAX_NUM):
        if prime_list[i] == 0:
            continue
        for j in range(2, 1501):
            if i*j > 3000:
                break
            prime_list[i*j] = 0
        
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if prime_list[nums[i]+nums[j]+nums[k]]:
                    answer = answer+1
        
    return answer