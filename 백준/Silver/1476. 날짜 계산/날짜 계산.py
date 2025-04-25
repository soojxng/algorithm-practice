E, S, M = map(int, input().split())
E = 0 if E == 15 else E
S = 0 if S == 28 else S
M = 0 if M == 19 else M
y = 1
while 1:
    if y % 15 == E and y % 28 == S and y % 19 == M:
        print(y)
        break
    y += 1