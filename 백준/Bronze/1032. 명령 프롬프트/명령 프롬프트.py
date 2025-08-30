n = int(input())
ans = list(input().rstrip())

for _ in range(n-1):
    tmp = input().rstrip()
    for i in range(len(ans)):
        if ans[i] != tmp[i]:
            ans[i] = '?'

print(''.join(ans))