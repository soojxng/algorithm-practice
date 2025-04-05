n = int(input())

a = [0, 1, 3] + [0]*(0 if n < 3 else n - 2)

for i in range(3, n + 1):
    a[i] = (a[i-1] + (2 * a[i-2])) % 10007

print(a[n])