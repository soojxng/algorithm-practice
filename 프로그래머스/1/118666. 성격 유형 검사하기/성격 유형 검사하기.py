def solution(survey, choices):
    d = {'RT':0, 'TR':0, 'CF':0, 'FC':0, 'JM':0, 'MJ':0, 'AN':0, 'NA':0}
    for k, v in zip(survey, choices):
        d[k] += v-4
    answer = ('R' if d['RT']-d['TR'] <= 0 else 'T') + ('C' if d['CF']-d['FC'] <= 0 else 'F') + ('J' if d['JM']-d['MJ'] <= 0 else 'M') + ('A' if d['AN']-d['NA'] <= 0 else 'N')
    return answer