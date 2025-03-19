import sys
input = sys.stdin.readline
A = ['-']
for i in range(12):
    tmp = A[i] + ' '*len(A[i]) + A[i]
    A.append(tmp)
while 1:
    try:
        N = int(input())
        print(A[N])
    except:
        break