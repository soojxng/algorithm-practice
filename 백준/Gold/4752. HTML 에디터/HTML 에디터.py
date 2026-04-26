import sys
input = sys.stdin.readline

while 1:
    text = input().rstrip()
    if text == '-1 -1':
        break
    b, e, text = text.split(' ', 2)
    b = int(b)
    e = int(e)

    s = []
    ans = []
    is_tag = 0
    i = 0
    while i < len(text):
        if b >= 0 and i >= b:
            for tag in s:
                ans.append('<')
                ans.append(tag)
                ans.append('>')
            b = -1
        elif i >= e:
            break

        if text[i] == '<':
            i += 1
            if text[i] == '/':
                i += 1
            tag = []
            while text[i] != '>':
                tag.append(text[i])
                i += 1
            tag = ''.join(tag)
            if s and s[-1] == tag:
                if b <= i < e:
                    ans.append('</')
                    ans.append(tag)
                    ans.append('>')
                s.pop()
            else:
                if b <= i < e:
                    ans.append('<')
                    ans.append(tag)
                    ans.append('>')
                s.append(tag)
        elif b <= i < e:
            ans.append(text[i])
        i += 1
        
    while s:
        ans.append('</')
        ans.append(s.pop())
        ans.append('>')
        
    print(''.join(ans))