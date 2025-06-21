import sys

def check_row(x, n):
    if n not in sudoku[x]:
        return 1
    else: return 0
    
def check_column(y, n):
    for i in range(9):
        if sudoku[i][y] == n:
            return 0
    return 1

def check_square(x, y, n):
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if sudoku[i][j] == n:
                return 0
    return 1

def fill(i):
    if i >= len(zeros):
        for s in sudoku:
            print(''.join(map(str, s)))
        sys.exit()
    else:
        x, y = zeros[i]
        for n in range(1, 10):
            if check_row(x, n) and check_column(y, n) and check_square(x//3, y//3, n):
                sudoku[x][y] = n
                fill(i+1)
                sudoku[x][y] = 0
            

sudoku = [list(map(int, list(input().rstrip()))) for _ in range(9)]
zeros = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))
            
fill(0)