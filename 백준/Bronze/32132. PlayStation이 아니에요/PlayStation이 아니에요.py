N = int(input())
ps = 0
ans = ''

for i in input().strip():
    if i == 'P':
        ps = 1
    elif ps == 1 and i =='S':
        ps = 2
    elif ps == 2 and (i == '4' or i == '5'):
        continue
    else: ps = 0
    ans += i

print(ans)