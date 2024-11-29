def solution(keymap, targets):
    answer = []
    min_key = {}
    for i in range(ord('A'), ord('Z')+1):
        min_key[chr(i)] = 101
        
    for k in keymap:
        for n in range(len(k)):
            if min_key[k[n]] > n + 1:
                min_key[k[n]] = n + 1
                
    for t in targets:
        cnt = 0
        for w in t:
            if min_key[w] == 101:
                cnt = -1
                break
            cnt += min_key[w]
        answer.append(cnt)
        
    return answer