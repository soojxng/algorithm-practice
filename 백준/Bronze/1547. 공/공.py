cups = [0, 1, 0, 0]

for _ in range(int(input())):
    x, y = map(int, input().split())
    if cups[x] != cups[y]:
        cups[x], cups[y] = cups[y], cups[x]

for i in range(len(cups)):
    if cups[i]:
        print(i)
        break