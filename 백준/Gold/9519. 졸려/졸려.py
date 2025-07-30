x = int(input())
s = input().rstrip()
n = len(s)
arr = [s]
while 1:
    tmp = ''
    for i in range(0, n, 2):
        tmp += s[i]
    for i in range(n-1 if n % 2 == 0 else n-2, -1, -2):
        tmp += s[i]
    if tmp == arr[0]:
        break
    arr.append(tmp)
    s = tmp
    
print(arr[x % len(arr)])