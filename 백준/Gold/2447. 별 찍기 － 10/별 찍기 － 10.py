import sys
input = sys.stdin.readline

N = int(input())
S = [['*' for _ in range(N)] for _ in range(N)]

def makeStar(a, b, N):
    if N != 1:
        tmp = N // 3
        for i in range(a + tmp, a + tmp*2):
            for j in range(b + tmp, b + tmp*2):
                S[i][j] = ' '
        for k in range(3):
            for l in range(3):
                if k != 1 or l != 1:
                    makeStar(a + k * tmp, b + l * tmp, tmp)
        
makeStar(0, 0, N)
for s in S:
    print(''.join(s))

