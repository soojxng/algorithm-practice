import sys
import re
input = sys.stdin.readline

stoi = {'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9'
        }
alpha = stoi.keys()
telephone = dict()

n = int(input())
for _ in range(n):
    s = input().rstrip()
    s = re.findall(r'[A-Z0-9]', s)
    tmp = ''
    for i in range(7):
        if s[i] in alpha:
            tmp += stoi[s[i]]
        else:
            tmp += s[i]
        if len(tmp) == 3:
            tmp += '-'
    if tmp in telephone:
        telephone[tmp] += 1
    else:
        telephone[tmp] = 1

if len(telephone) == n:
    print('No duplicates.')
else:
    for t in sorted(telephone.keys()):
        if telephone[t] > 1:
            print(t, telephone[t])