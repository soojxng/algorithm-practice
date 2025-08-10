minn, maxx = map(int, input().split())
checked = [1]*(maxx-minn+1)
for i in range(2, 1000001):
    ii = i*i
    if ii > maxx:
        break
    s = ((minn + ii - 1) // ii)*ii
    for j in range(s, maxx+1, ii):
        checked[j-minn] = 0
print(sum(checked))