def solution(number, limit, power):
    answer = 0
    
    arr = [1 for _ in range(number)]
    
    for i in range(2, number+1):
        for j in range(i, number+1, i):
            arr[j-1] += 1
            
    answer = [k if k <= limit else power for k in arr]

    return sum(answer)