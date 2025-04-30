import sys
import ast
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()
    n = int(input())
    arr = ast.literal_eval(input().strip())
    r = 0
    s = 0
    e = 0
    for i in p:
        if i == 'R':
            r = not r
        elif i == 'D' and s + e == n:
            print('error')
            break
        elif i == 'D':
            if r: e += 1
            else: s += 1
    else:
        arr = arr[s:n-e]
        if r: arr = arr[::-1]
        print(f"[{','.join(map(str, arr))}]")