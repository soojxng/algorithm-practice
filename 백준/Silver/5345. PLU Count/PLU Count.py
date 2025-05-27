import sys
input = sys.stdin.readline

PLU = ['pP', 'lL', 'uU']

for _ in range(int(input())):
    cnt = 0
    for x in input().rstrip():
        if x in PLU[cnt%3]:
            cnt += 1
    print(cnt // 3)