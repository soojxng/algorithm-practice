def solution(n):
    answer = 0
    li = [1 for _ in range(n+1)]
    for i in range(2, n//2+1):
        for j in range(2, n//2+1):
            if i*j > n:
                break
            if li[i*j] == 1:
                li[i*j] = 0
    answer = sum(li[2:n+1])
    return answer
