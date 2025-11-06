import sys
input = sys.stdin.readline

n = int(input())
hexa = [1]
i = 1
while 1:
    x = hexa[-1] + (i*4+1)
    if x > n:
        break
    hexa.append(x)
    i += 1

if n <= 146858:
    ans = [i for i in range(n+1)]

    for h in hexa[1:]:
        for i in range(h, min(h*5+1, n+1)):
            ans[i] = min(ans[i], ans[i-h]+1)

    print(ans[n])
else:
    if n in hexa:
        print(1)
    else:
        ans = 3
        for a in hexa:
            if ans == 2:
                break
            for b in hexa:
                if a + b > n:
                    break
                elif a + b == n:
                    ans = 2
                    break
        print(ans)