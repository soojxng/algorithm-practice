def solution(s):
    answer = 0
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    for i in range(len(num)):
        s = s.replace(num[i], str(i))
    return int(s)