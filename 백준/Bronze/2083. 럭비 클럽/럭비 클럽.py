while 1:
    tmp = list(input().strip().split())
    if tmp[0] == '#' and tmp[1] == tmp[2] == '0':
        break
    if int(tmp[1]) > 17 or int(tmp[2]) >= 80:
        print(tmp[0], 'Senior')
    else:
        print(tmp[0], 'Junior')