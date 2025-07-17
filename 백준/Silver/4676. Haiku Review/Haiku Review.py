import sys
input = sys.stdin.readline

d = {0: 5, 1: 7, 2: 5}
vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
while 1:
    haiku = input().rstrip().split('/')
    if haiku[0] == 'e' and haiku[1] == 'o' and haiku[2] == 'i':
        break
    for i in range(3):
        f = 0
        cnt = 0
        for x in haiku[i]:
            if x in vowels and f == 0:
                cnt += 1
                f = 1
            elif x in vowels:
                continue
            elif f:
                f = 0
        if cnt != d[i]:
            print(i+1)
            break
    else:
        print('Y')