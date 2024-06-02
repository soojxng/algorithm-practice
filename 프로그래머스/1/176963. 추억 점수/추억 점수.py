def solution(name, yearning, photo):
    answer = []
    miss = dict(zip(name, yearning))
    
    for i in photo:
        tmp = 0
        for j in i:
            tmp += miss[j] if j in name else 0
        answer.append(tmp)
    return answer