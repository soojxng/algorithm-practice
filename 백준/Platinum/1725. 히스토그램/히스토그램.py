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

n = int(input())
s = [[0, 0]]
ans = 0
for _ in range(n):
    tmp = int(input())
    if tmp > s[-1][0]:
        s.append([tmp, 1])
    elif tmp == s[-1][0]:
        s[-1][1] += 1
    else:
        ans = cal(tmp, ans)
ans = cal(0, ans)
print(ans)