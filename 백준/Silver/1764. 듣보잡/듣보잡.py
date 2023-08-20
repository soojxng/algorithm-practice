n, m =map(int, input().split())
s1 = set()
s2 = set()
for _ in range(n):
    s1.add(input())
for _ in range(m):
    s2.add(input())
s3 = s1&s2
print(len(s3))
s3 = list(s3)
s3.sort()
for i in s3:
    print(i)