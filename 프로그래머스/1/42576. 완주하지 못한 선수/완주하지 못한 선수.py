def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            answer = p
            break
    if answer == '':
        answer = participant[-1]
    return answer