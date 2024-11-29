def solution(N, stages):
    M = len(stages)
    
    stop_num = [0 for _ in range(N+1)]
    for s in stages:
        stop_num[s-1] += 1

    p = [2]+[0 for _ in range(N)]
    for i in range(1, N+1):
        p[i] = 0 if M == 0 else stop_num[i-1]/M
        M = M - stop_num[i-1]

    answer = sorted(range(len(p)), key=lambda k: p[k],reverse=True)[1:]
    
    return answer