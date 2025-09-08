n = int(input())
t = input().rstrip()
s = []
ans = []
for i in range(n-1, -1, -1):
    if s and s[-1] == t[i]:
        s.pop()
        ans.append('N')
    elif t[i] == 'U':
        ans.append('SN')
        s.append('S')
    elif t[i] == 'S':
        ans.append('UN')
        s.append('U')

ans = ''.join(ans)
print(len(ans))
print(ans)