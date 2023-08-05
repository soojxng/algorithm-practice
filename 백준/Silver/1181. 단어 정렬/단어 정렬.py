n = int(input())
li = [[] for _ in range(51)]
for _ in range(n):
    s = input()
    if s not in li[len(s)]:
        li[len(s)].append(s)
for i in li:
    i.sort()
    for j in i:
        print(j)