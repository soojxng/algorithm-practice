n = int(input())
s = set()
while n > 1:
    if n in s:
        print('NIE')
        break
    s.add(n)
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * (n+1)
else:
    print('TAK')