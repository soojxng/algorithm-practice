n = int(input())
S1 = set([i*i for i in range(1, int(n**0.5)+1)])
S2 = set()

if n in S1:
    print(1)
else:
    for i in S1:
        for j in S1:
            S2.add(i+j)
    if n in S2:
        print(2)
    else:
        for s in S1:
            if n-s in S2:
                print(3)
                break
        else:
            print(4)