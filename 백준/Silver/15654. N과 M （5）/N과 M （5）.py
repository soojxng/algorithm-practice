def bt():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    
    for i in nums:
        if i in tmp:
            continue
        tmp.append(i)
        bt()
        tmp.pop()
    

tmp = []
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

bt()