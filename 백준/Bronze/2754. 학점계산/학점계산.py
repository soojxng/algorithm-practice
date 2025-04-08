score = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0.0, '+': 0.3, '0':0.0, '-':-0.3}

C = input().strip()

print(sum(score[i] for i in C))