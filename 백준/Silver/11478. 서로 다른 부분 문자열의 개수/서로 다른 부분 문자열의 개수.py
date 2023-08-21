s = input()
sub = set()
for i in range(len(s) +1):
    for j in range(i):
        sub.add(s[j:i])
print(len(sub))