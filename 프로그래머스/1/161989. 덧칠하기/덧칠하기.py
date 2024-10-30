def solution(n, m, section):
    answer = 0
    paint_list = [1 for _ in range(n)]
    for i in section:
        paint_list[i - 1] = 0
    
    j = 0
    while j < n:
        if paint_list[j] == 0:
            j += m
            answer += 1
        else:
            j += 1
    return answer