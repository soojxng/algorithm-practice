import sys
input = sys.stdin.readline

k = int(input())
d = {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}

for x in range(1, k+1):
    l = input().rstrip()
    s = []
    for a in l:
        if s and s[-1] == d[a]:
            s.pop()
        else:
            s.append(a)
            
    print(f'Data Set {x}:')
    print('Yes' if not s else 'No')
    if x != k:
        print()