def solution(k, score):
    legend = [score[0]]
    answer = [score[0]]
    
    for i in score[1:]:
        legend.append(i)
        if len(legend) > k:
            legend.remove(min(legend))
        answer.append(min(legend))
    return answer