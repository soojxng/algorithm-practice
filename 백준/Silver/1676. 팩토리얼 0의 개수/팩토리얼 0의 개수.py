N = int(input())
f = 5
cnt = 0

while N >= f:
    cnt += N // f
    f *= 5
    
print(cnt)