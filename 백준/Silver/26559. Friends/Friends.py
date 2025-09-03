import sys
input = sys.stdin.readline

for t in range(int(input())):
    friend = []
    for _ in range(int(input())):
        name, like = input().rstrip().split()
        friend.append((int(like), name))
    friend.sort(reverse=True)
    friend = [n for l, n in friend]
    print(', '.join(friend))