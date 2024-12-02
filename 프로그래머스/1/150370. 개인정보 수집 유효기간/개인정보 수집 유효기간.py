def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    tod = today.split('.')
    tt = int(tod[0])*336 + int(tod[1])*28 + int(tod[2])
    
    for term in terms:
        t, m = term.split(' ')
        term_dict[t] = int(m)*28
    
    for i in range(len(privacies)):
        d, t = privacies[i].split(' ')
        dat = d.split('.')
        dd = int(dat[0])*336 + int(dat[1])*28 + int(dat[2]) + term_dict[t]
        if dd <= tt:
            answer.append(i+1)
        
    return answer