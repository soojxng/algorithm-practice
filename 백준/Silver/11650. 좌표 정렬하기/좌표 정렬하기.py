n = int(input())
li = []
for i in range(n):
    a, b = map(int, input().split())
    li.append([a, b])
li.sort()
for i in li:
    a, b =map(int, i)
    print(a, b)