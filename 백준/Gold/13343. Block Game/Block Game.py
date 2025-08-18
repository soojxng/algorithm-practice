a, b = map(int, input().split())
if b < a: a, b = b, a
cnt = True
while 1:
    if b >= 2 * a:
        break
    a, b = b % a, a
    if a == 0 or b == 0:
        break
    cnt = not cnt
print('win' if cnt else 'lose')