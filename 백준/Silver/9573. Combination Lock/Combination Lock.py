N = int(input())
johns = list(map(int, input().split()))
masters = list(map(int, input().split()))
s = set()

def calRange(num):
    return [(num + x) % N for x in range(-2, 3)]

for i in calRange(johns[0]):
    for j in calRange(johns[1]):
        for k in calRange(johns[2]):
            s.add((i, j, k))

for i in calRange(masters[0]):
    for j in calRange(masters[1]):
        for k in calRange(masters[2]):
            s.add((i, j, k))
            
print(len(s))