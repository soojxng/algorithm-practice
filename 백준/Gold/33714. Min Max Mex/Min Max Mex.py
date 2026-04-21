import sys
input = sys.stdin.readline
 
n, k = map(int, input().split())
a = list(map(int, input().split()))
d = dict()

for x in a:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

i = 0
min_val = 0
max_val = k

while 1:
    if i not in d:
        min_val = i
        break
    if d[i] <= k:
        min_val = i
        break
    i += 1

for x in sorted(d.keys()):
    if x <= max_val:
        max_val += 1
    else:
        break

print(min_val)
print(max_val)