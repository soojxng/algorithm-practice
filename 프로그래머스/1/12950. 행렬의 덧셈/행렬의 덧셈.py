def sum_arr(a, b):
    tmp = []
    for i, j in zip(a, b):
        tmp.append(i+j)
    return tmp

def solution(arr1, arr2):
    tmp = []
    for i, j in zip(arr1, arr2):
        tmp.append(sum_arr(i, j))
    return tmp