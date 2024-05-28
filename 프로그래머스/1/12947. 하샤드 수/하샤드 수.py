def solution(x):
    answer = True
    n = x
    x_sum = 0
    
    while x > 0:
        x_sum += (x%10)
        x //= 10
        
    answer = (n/x_sum == n//x_sum)
    return answer