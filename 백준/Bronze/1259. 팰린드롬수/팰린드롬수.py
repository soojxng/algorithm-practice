import sys
input = sys.stdin.readline

while 1:
    tmp = input().strip()
    f = 1
    if tmp == '0':
        break
    for i in range(len(tmp)//2):
        if tmp[i] != tmp[-(i+1)]:
            f = 0
            break
    print('yes' if f else 'no')