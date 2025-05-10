N = int(input())

tmp = [1, 2]
for i in range(0, N-2):
    j = i % 2
    tmp[j] = (tmp[j-1] + tmp[j]) % 15746
print(tmp[not N%2])