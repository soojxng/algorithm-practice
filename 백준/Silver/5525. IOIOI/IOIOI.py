N = int(input())
M = int(input())
S = input().strip()
cnt = 0
i = 0
while i < M - 1:
    if S[i] == 'I':
        tmp = 0
        while i + 2 < M and S[i+1] == 'O' and S[i+2] == 'I':
            tmp += 1
            i += 2
        cnt += tmp - (N-1) if tmp >= N else 0
    i += 1
print(cnt)