def solution(new_id):
    answer = ''
    able = 'abcdefghijklnmopqrstuvwxyz0123456789-_.'
    new_id = new_id.lower()

    for i in new_id:
        if i not in able:
            continue
        if i == '.' and (len(answer) == 0 or answer[-1] == '.'):
            continue
        answer += i
    
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15] if answer[14] != '.' else answer[:14]
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
        
    return answer