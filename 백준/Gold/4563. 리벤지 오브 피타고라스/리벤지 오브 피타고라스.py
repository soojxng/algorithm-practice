import sys
input = sys.stdin.readline

while 1:
    a = int(input())
    if a == 0:
        break
    ans = 0
    a2 = a*a
    for i in range(1, a):
        if a2 % i == 0:
            tmp = a2//i - i
            if tmp % 2 == 0 and tmp // 2 > a:
                ans += 1
    print(ans)