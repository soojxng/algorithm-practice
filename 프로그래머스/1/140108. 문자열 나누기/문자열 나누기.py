def solution(s):
    answer = 0
    start = 0
    while len(s) > start:
        tmp = 0
        for i in range(start, len(s)):
            tmp += 1 if s[start] == s[i] else -1
            if tmp == 0:
                start = i + 1
                break
        answer += 1
        if tmp != 0:
            break
    return answer