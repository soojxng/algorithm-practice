n = int(input())
s1 = set(map(int, input().split()))
m = int(input())
li = list(map(int, input().split()))

for i in li:
    if i in s1:
        print("1", end = ' ')
    else:
        print("0", end=' ')