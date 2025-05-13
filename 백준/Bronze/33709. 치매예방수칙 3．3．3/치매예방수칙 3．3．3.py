N = int(input())
ans = 0
for i in input().strip().split('.'):
    if i.isdigit():
        ans += int(i)
    else:
        for j in i.split('|'):
            if j.isdigit():
                ans += int(j)
            else:
                for k in j.split(':'):
                    if k.isdigit():
                        ans += int(k)
                    else:
                        for l in k.split('#'):
                            ans += int(l)
print(ans)