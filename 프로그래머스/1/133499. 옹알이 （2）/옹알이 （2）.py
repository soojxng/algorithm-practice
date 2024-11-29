def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        for j in can:
            i = i.replace(j*2, '.')
            i = i.replace(j, '0')
        if i.isdigit():
            answer += 1
            
    return answer