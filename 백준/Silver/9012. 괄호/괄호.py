T = int(input())

for _ in range(T):
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            if cnt < 1:
                cnt = -1
                break
            cnt -= 1
    if cnt != 0:
        print("NO")
    else:
        print("YES")