import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
arr = [0]*max(A).bit_length()

for a in A:
    for i in range(a.bit_length()):
        arr[i] += (a>>i) & 1
    
print(max(arr))