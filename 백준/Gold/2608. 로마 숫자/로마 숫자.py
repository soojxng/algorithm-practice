import sys
input = sys.stdin.readline

def romToNum(r):
    i = 0
    n = 0
    while i < len(r):
        if i < len(r) - 1 and d[r[i]] < d[r[i+1]]:
            n += d[r[i+1]] - d[r[i]]
            i += 2
        else:
            n += d[r[i]]
            i += 1
    return n

def numToRom(n):
    r = ''
    for x, y in li:
        if n >= y:
            r += x*(n//y)
            n %= y
    return r

d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
li = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90],
     ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
a = input().rstrip()
b = input().rstrip()
c = romToNum(a) + romToNum(b)
print(c)
print(numToRom(c))