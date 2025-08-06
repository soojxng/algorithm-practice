s = []
tmp = input().rstrip()
pb = input().rstrip()
n = len(pb)

for t in tmp:
    s.append(t)
    if t == pb[-1] and len(s) >= n:
        for i in range(n):
            if s[-n+i] != pb[i]:
                break
        else:
            for _ in range(n):
                s.pop()
print(''.join(s) if s else 'FRULA')