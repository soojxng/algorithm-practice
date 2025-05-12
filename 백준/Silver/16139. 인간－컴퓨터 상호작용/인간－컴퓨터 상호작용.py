import sys
input = sys.stdin.readline

S = input().strip()
arr = [[0]*26 for _ in range(len(S))]
for i in range(len(S)):
    if i > 0: arr[i] = arr[i-1][:]
    arr[i][ord(S[i])-97] += 1
    
for _ in range(int(input())):
    tmp = list(input().strip().split())
    print(arr[int(tmp[2])][ord(tmp[0])-97] - (arr[int(tmp[1])-1][ord(tmp[0])-97] if int(tmp[1])-1 >= 0 else 0))