N = int(input())

if N == 1:
    print(0)
else:
    if N % 2 == 0:
        print(N*N//2)
    else:
        print(N*N//2+1)