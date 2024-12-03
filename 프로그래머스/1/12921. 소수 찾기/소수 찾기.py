def solution(n):
    answer = 0
    li = [1 for _ in range(1000001)]
    for i in range(2, 500000):
        for j in range(2, 500000):
            if i*j > 1000000:
                break
            if li[i*j] == 1:
                li[i*j] = 0
    answer = sum(li[2:n+1])
    return answer