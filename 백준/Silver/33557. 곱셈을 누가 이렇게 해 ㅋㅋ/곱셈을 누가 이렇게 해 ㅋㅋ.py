import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = input().strip().split()
    C = ''
    D = int(A)*int(B)
    if len(B) > len(A): A, B = B, A
    B = B.rjust(len(A), '1')
    for i in range(len(A)):
        C += str(int(A[i])*int(B[i]))
    if int(C) == D:
        print(1)
    else: print(0)