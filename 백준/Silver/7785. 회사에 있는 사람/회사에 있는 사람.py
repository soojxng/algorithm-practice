n = int(input())
s = set()
for _ in range(n):
    name, commute = input().split()
    if commute == 'enter':
        s.add(name)
    elif commute == 'leave':
        s.remove(name)
s = list(s)
s.sort()
s.reverse()
for i in s:
    print(i)