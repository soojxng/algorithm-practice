import sys
input = sys.stdin.readline

s = list(input().rstrip().split())
haiku = (5, 7, 5)
vowel = {'a', 'e', 'i', 'o', 'u', 'y'}
alpha = set(list('qwertyuiopasdfghjklzxcvbnm'))
ans = [0]

tmp = 0
f = 1
for i in range(len(s)):
    if len(ans) == 4:
        f = 0
        break
    cnt = 0
    w = s[i].lower()
    n = len(w)
    for j in range(n-1, -1, -1):
        if w[j] in alpha:
            n = j+1
            break
    j = 0
    c = -1
    while j < n:
        if w[j] == 'q' and j < n-1 and w[j+1] == 'u':
            c += 1
            j += 1
        elif w[j] == 'y' and j < n-1 and w[j+1] != 'y' and w[j+1] in vowel:
            c += 1
        elif j == n-1 and w[j] == 'e' and j != 0 and w[j-1] == 'l' and c >= 2:
            cnt += 1
        elif j == n-1 and w[j] == 'e':
            break
        elif j == n-2 and w[j] == 'e' and w[j+1] == 's':
            if c >= 2:
                cnt += 1
        elif w[j] in vowel:
            if c != 0:
                cnt += 1
            c = 0
        elif c == -1:
            c = 1
        else:
            c += 1
        j += 1
    
    tmp += cnt if cnt > 0 else 1
    if tmp > haiku[len(ans)-1]:
        f = 0
        break
    elif tmp == haiku[len(ans)-1]:
        tmp = 0
        ans.append(i+1)
    
if not f or len(ans) < 4:
    print(' '.join(s))
else:
    for i in range(3):
        print(*s[ans[i]:ans[i+1]])