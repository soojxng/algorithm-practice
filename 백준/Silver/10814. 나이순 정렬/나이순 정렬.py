n = int(input())
li = [[] for _ in range(201)]
for i in range(n):
    a, b = input().split()
    li[int(a)].append(b)
for i in li:
    for j in i:
        print(li.index(i), j)