N = int(input())
A = list(map(int, input().split()))
arr = [A[0]]

def bs(x):
    s, e = 0, len(arr)-1
    tmp = 0
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] < x: s = mid + 1
        else:
            tmp = mid
            e = mid - 1
        
    return tmp

for a in A:
    if a > arr[-1]: arr.append(a)
    else: arr[bs(a)] = a
    
print(len(arr))