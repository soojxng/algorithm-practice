import sys
input = sys.stdin.readline     

dic = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
d = ((2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2))
checked = [[0]*6 for _ in range(6)]
valid = 1
path = []
for i in range(36):
    tmp = input().rstrip()
    x = dic[tmp[0]]
    y = int(tmp[1])-1
    path.append((x, y))
    
for i in range(36):
    x, y = path[i]
    if checked[x][y] == 1:
        valid = 0
        break
    checked[x][y] = 1
    x2, y2 = path[i-1]
    f = 0
    for dx, dy in d:
        if x2 + dx == x and y2 + dy == y:
            f = 1
    if f == 0:
        valid = 0
        break
print("Valid" if valid else "Invalid")
