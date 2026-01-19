import sys
input = sys.stdin.readline
    
def readBits(i, cnt):
    return i+cnt, int(b[i:i+cnt], 2)

def numeric(i):
    i, cnt = readBits(i, 10)
    for _ in range(cnt//3):
        i, tmp = readBits(i, 10)
        for x in f'{tmp:03d}':
            results.append(x)
    if cnt % 3 == 2:
        i, tmp = readBits(i, 7)
        for x in f'{tmp:02d}':
            results.append(x)
    elif cnt % 3 == 1:
        i, tmp = readBits(i, 4)
        results.append(str(tmp))
    return i

def alphanumeric(i):
    i, cnt = readBits(i, 9)
    for _ in range(cnt//2):
        i, tmp = readBits(i, 11)
        results.append(a[tmp//45])
        results.append(a[tmp%45])
    if cnt % 2 == 1:
        i, tmp = readBits(i, 6)
        results.append(a[tmp])
    return i

def bit8byte(i):
    i, cnt = readBits(i, 8)
    for _ in range(cnt):
        i, tmp = readBits(i, 8)
        if tmp == 96:
            tmp = '\\'
        elif tmp == 35:
            tmp = '\\#'
        elif 20 <= tmp <= 126:
            tmp = chr(tmp)
        else:
            tmp = ('\\' + format(tmp, '02X'))
        results.append(tmp)
    return i

def kanji(i):
    i, cnt = readBits(i, 8)
    for _ in range(cnt):
        i, tmp = readBits(i, 13)
        tmp = '#' + format(tmp, '04X')
        results.append(tmp)
    return i

a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:'

p = int(input())
for _ in range(p):
    s = input().rstrip()
    b = ''
    for x in s:
        b += format(int(x, 16), '04b')

    i = 0
    cnt = 0
    results = []
    while i < len(b):
        m = b[i:min(i+4, len(b))]
        i += 4
        if m == '0001':
            i = numeric(i)
        elif m == '0010':
            i = alphanumeric(i)
        elif m == '0100':
            i = bit8byte(i)
        elif m == '1000':
            i = kanji(i)
        else:
            break

    print(len(results), ''.join(results))