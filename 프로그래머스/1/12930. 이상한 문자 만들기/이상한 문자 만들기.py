def solution(s):
    answer = ''
    arr = s.split(' ')
    for i in range(len(arr)):
        tmp = ''
        for j in range(len(arr[i])):
            if j%2 == 0:
                tmp += arr[i][j].upper()
            else:
                tmp += arr[i][j].lower()
        answer += tmp + ' '
    return answer[:-1]