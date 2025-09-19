import sys
input = sys.stdin.readline

def cal(x):
    if x == 'B':
        return 1
    else: return 0

var = [0, 0]
while 1:
    f = 0
    tmp = list(input().split())
    if tmp[0] == '7':
        break
    elif tmp[0] == '1':
        f = cal(tmp[1])
        var[f] = int(tmp[2])
    elif tmp[0] == '2':
        f = cal(tmp[1])
        print(var[f])
    elif tmp[0] == '3':
        f = cal(tmp[1])
        g = cal(tmp[2])
        var[f] += var[g]
    elif tmp[0] == '4':
        f = cal(tmp[1])
        g = cal(tmp[2])
        var[f] *= var[g]
    elif tmp[0] == '5':
        f = cal(tmp[1])
        g = cal(tmp[2])
        var[f] -= var[g]
    elif tmp[0] == '6':
        f = cal(tmp[1])
        g = cal(tmp[2])
        var[f] //= var[g]