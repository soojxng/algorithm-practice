import sys
input = sys.stdin.readline

s = input().rstrip()
st = []
q = 0
k = 0
for x in s:
    if x == '(':
        st.append((k, q-1))
        q = 0
    elif x == ')':
        k, tmp = st.pop()
        q = int(k)*q + tmp
    else:
        q += 1
        k = x
print(q)
