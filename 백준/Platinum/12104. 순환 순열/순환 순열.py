import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
b += b

ai = [0]*len(a)
j = 0
for i in range(1, len(a)):
    while j > 0 and a[i] != a[j]:
        j = ai[j-1]
    if a[i] == a[j]:
        j += 1
        ai[i] = j

cnt = 0
j = 0
for i in range(len(b)):
    while j > 0 and b[i] != a[j]:
        j = ai[j-1]
    if b[i] == a[j]:
        if j == len(a)-1:
            if 0 <= i - len(a) + 1 < len(a):
                cnt += 1
            j = ai[j]
        else:
            j += 1
            
print(cnt)