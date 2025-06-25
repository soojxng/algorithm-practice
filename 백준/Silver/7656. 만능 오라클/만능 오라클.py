questions = input()

s, e = -1, -1
while questions.find('What', e+1) != -1:
    s = questions.find('What', e+1)
    e = questions.find('?', s+1)
    ans = questions[s+4:e]
    if ans.find('.') != -1:
        e = questions.find('.', s+1)
    else:
        print('Forty-two' + ans + '.')