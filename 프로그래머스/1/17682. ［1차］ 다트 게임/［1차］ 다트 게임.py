import re

def solution(dartResult):
    dart_list = re.split(r'([SDT#*])', dartResult)
    point_list = []
    for d in dart_list:
        if d.isdigit():
            point_list.append(int(d))
        elif d == 'S':
            point_list[-1] **= 1
        elif d == 'D':
            point_list[-1] **= 2
        elif d == 'T':
            point_list[-1] **= 3
        elif d == '#':
            point_list[-1] *= -1
        elif d == '*':
            point_list[-1] *= 2
            if len(point_list) > 1:
                point_list[-2] *= 2
        print(point_list)
    return sum(point_list)