import sys
input = sys.stdin.readline

words = []

while 1:
    word = input().rstrip()

    if word == '-':
        break

    tmp = [0]*26

    for w in word:
        x = ord(w) - ord('A')
        tmp[x] += 1

    words.append(tmp)

while 1:
    board = input().rstrip()

    if board == '#':
        break

    tmp = [0]*26
    
    for b in board:
        x = ord(b) - ord('A')
        tmp[x] += 1
    
    result = [0]*26
    
    for word in words:
        f = 1
        for i in range(26):
            if word[i] > tmp[i]:
                f = 0
                break
        if f:
            for i in range(26):
                if word[i]:
                    result[i] += 1

    min_ans = []
    min_val = float('inf')
    max_ans = []
    max_val = 0

    for i in range(26):
        if not tmp[i]:
            continue

        if result[i] < min_val:
            min_val = result[i]
            min_ans = [chr(i + ord('A'))]
        elif result[i] == min_val:
            min_ans.append(chr(i + ord('A')))

        if result[i] > max_val:
            max_val = result[i]
            max_ans = [chr(i + ord('A'))]
        elif result[i] == max_val:
            max_ans.append(chr(i + ord('A')))

    print(''.join(min_ans), min_val, ''.join(max_ans), max_val)