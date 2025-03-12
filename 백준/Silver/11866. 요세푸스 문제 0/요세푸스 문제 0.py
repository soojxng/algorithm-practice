n, k = map(int, input().split())

c = list(range(1, n + 1))
p = []  #요세푸스 순열 저장

f = 0
while n > 0:
    f = (f + k - 1) % len(c)
    p.append(str(c.pop(f)))
    n -= 1

answer = '<' + ', '.join(p) + '>'
print(answer)
