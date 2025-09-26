import sys
input = sys.stdin.readline

n, h = map(int, input().split())
pref = [0]*(h+1)
for i in range(n):
    x = int(input())
    if i % 2 == 0:
        pref[1] += 1
        pref[x] -= 1
    else:
        pref[h-x] += 1

min_obs = float('inf')
obs_num = 0
for i in range(1, h+1):
    pref[i] += pref[i-1]
    if min_obs > pref[i]:
        min_obs = pref[i]
        obs_num = 1
    elif min_obs == pref[i]:
        obs_num += 1

print(min_obs, obs_num)
