n = int(input())
li = []
for i in range(n):
    a, b = map(int, input().split())
    li.append([b, a])
li.sort()
for i in li:
    b, a =map(int, i)
    print(a, b)