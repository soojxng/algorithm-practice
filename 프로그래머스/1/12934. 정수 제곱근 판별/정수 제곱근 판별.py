def solution(n):
    answer = 0
    arr = []
    
    for i in range(1, 7200000, 1):
        arr.append(i**2)
        
    if n in arr:
        index_num = arr.index(n) + 1
        answer = arr[index_num]
    else:
        answer = -1
    
    return answer