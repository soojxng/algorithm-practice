import sys
input = sys.stdin.readline

def cal(tmp, ans):
    while s[-1][0] > tmp:
        h, cnt = s.pop()
        ans = max(ans, h*cnt)
        if s[-1][0] > tmp:
            s[-1][1] += cnt
        elif s[-1][0] == tmp:
            s[-1][1] += cnt+1
        else:
            s.append([tmp, cnt+1])
    
    return ans
while 1:
    tmp = list(map(int, input().split()))
    if len(tmp) == 1 and tmp[0] == 0:
        break
    
    s = [[0, 0]]
    ans = 0
    for x in tmp[1:]:
        if x > s[-1][0]:
            s.append([x, 1])
        elif x == s[-1][0]:
            s[-1][1] += 1
        else:
            ans = cal(x, ans)
    
    ans = cal(0, ans)
    print(ans)