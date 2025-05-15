def cal(i):
    if i == N:
        t_s[2] = min(t_s[2], abs(t_s[0]-t_s[1]))
        return
    else:
        for t in range(2):
            if len(teams[t]) >= N//2:
                continue
            tmp = 0
            for j in teams[t]:
                tmp += S[i][j] + S[j][i]
            t_s[t] += tmp
            teams[t].append(i)
            cal(i+1)
            t_s[t] -= tmp
            teams[t].pop()
            
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
teams = [[0], []]
t_s = [0, 0, float('inf')]
cal(1)
print(t_s[2])