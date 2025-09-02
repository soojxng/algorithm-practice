n = int(input())
arr = list(input().rstrip().split())
ans = [arr[0]]
for i in range(1, n):
    for j in range(i):
        if arr[i]+ans[j] > ans[j]+arr[i]:
            ans.insert(j, arr[i])
            break
    else:
        ans.append(arr[i])
        
if ans[0] == '0':
    print(0)
else:
    print(''.join(ans))