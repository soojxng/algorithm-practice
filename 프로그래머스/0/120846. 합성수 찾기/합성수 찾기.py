def solution(n):
    answer = 0
    arr = [1 for _ in range(101)]
    for i in range(2, 101):
        for j in range(i, 101, i):
            arr[j] += 1

    for i in range(1, n+1):
        if arr[i] > 2:
            answer += 1
    return answer