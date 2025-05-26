import sys

keyboards = dict()
tmp = ['=-0987654321`', '\][POIUYTREWQ', "';LKJHGFDSA", '/.,MNBVCXZ']
for t in tmp:
    for i in range(1, len(t)):
        keyboards[t[i-1]] = t[i]
keyboards[' '] = ' '

for line in sys.stdin:
    print(''.join(keyboards[x] for x in line.rstrip()))