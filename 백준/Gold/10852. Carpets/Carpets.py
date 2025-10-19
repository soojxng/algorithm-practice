import sys
input = sys.stdin.readline

def cut(fw, fh, cw, ch):
    if fw == cw and fh == ch:
        return []
    elif fw == cw:
        return [(fw, fh-ch)]
    elif fh == ch:
        return [(fw-cw, fh)]
    else:
        return [(cw, fh-ch), (fw-cw, fh)]


def put_carpets(floors, carpets):
    if len(floors) == 0:
        return 1
    if len(carpets) == 0:
        return 0
    
    fi, tmp = -1, -1
    for i, f in enumerate(floors):
        if f[1] > tmp:
            fi, tmp = i, f[1]
    while fi+1 < len(floors) and floors[fi][1] == floors[fi+1][1]:
        floors[fi:fi+2] = [(floors[fi][0]+floors[fi+1][0], floors[fi][1])]

    fw, fh = floors[fi]
    s = set()
    for i in range(len(carpets)):
        if carpets[i] in s:
            continue
        s.add(carpets[i])

        cw, ch = carpets[i]
        if cw <= fw and ch <= fh:
            if put_carpets(floors[0:fi] + cut(fw, fh, cw, ch) + floors[fi+1:], carpets[0:i] + carpets[i+1:]):
                return 1
        if cw != ch and ch <= fw and cw <= fh:
            if put_carpets(floors[0:fi] + cut(fw, fh, ch, cw) + floors[fi+1:], carpets[0:i] + carpets[i+1:]):
                return 1
    return 0

W, H = map(int, input().split())
C = int(input())
carpets = []
total = 0
for _ in range(C):
    a, w, h = map(int, input().split())
    w, h = (w, h) if w <= h else (h, w)
    for _ in range(a):
        carpets.append((w, h))
        total += w*h
carpets.sort(reverse=1)

if total < W*H:
    print('no')
else:
    print('yes' if put_carpets([(W, H)], carpets) else 'no')