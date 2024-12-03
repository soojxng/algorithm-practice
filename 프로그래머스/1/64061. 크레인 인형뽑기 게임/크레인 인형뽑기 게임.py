def solution(board, moves):
    answer = 0
    b = list(map(list, zip(*board[::-1])))
    b = [r if 0 not in r else r[:r.index(0)] for r in b]
    s = []
    for m in moves:
        if len(b[m-1]) > 0:
            s.append(b[m-1].pop())
            while len(s) > 1 and s[-1] == s[-2]:
                s.pop()
                s.pop()
                answer += 2    
    return answer