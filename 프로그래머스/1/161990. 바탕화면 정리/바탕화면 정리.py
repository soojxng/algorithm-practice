def solution(wallpaper):
    answer = [99, 99, -1, -1]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                answer[0] = i if answer[0] > i else answer[0]
                answer[1] = j if answer[1] > j else answer[1]
                answer[2] = i+1 if answer[2] < i+1 else answer[2]
                answer[3] = j+1 if answer[3] < j+1 else answer[3]
    return answer