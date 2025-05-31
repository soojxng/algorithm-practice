N = int(input())
A = list(map(int, input().split()))
A = sorted(list(enumerate(A)), key=lambda x : x[1])
tmp = [0] * N
for j, (i, a) in enumerate(A):
    tmp[i] = j
print(' '.join(map(str, tmp)))