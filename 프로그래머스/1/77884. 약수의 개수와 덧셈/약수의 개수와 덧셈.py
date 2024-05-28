def solution(left, right):
    answer = 0
    arr = [1 for _ in range(1001)]
    for i in range(2, 1001):
        for j in range(i, 1001, i):
            arr[j] += 1
    for k in range(left, right + 1):
        answer += k if (arr[k]) % 2 == 0 else -k
    return answer