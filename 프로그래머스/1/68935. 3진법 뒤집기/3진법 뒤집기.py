def solution(n):
    answer = []
    ans = 0
    while n > 0:
        answer.append(n%3)
        n = n//3
    for i in range(len(answer)):
        ans += answer[i] * (3 ** (len(answer)-i-1))
    return ans