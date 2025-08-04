n = int(input())
A = []
B = []
for i in range(n, 2, -3):
    A.append(i)
    B.append(i-1)
    B.append(i-2)
if n % 3 == 2:
    A.append(2)
    B.append(1)

print(len(A))
print(*A)
print(len(B))
print(*B)