import random

arr = list(range(1, 10001))
random.shuffle(arr)

for a in arr:
    # A가 a인지 물어보고 flush를 한다.
    # print에 flush 파라미터를 넣으면 된다.
    print("? A", a, flush=True)

    # 채점기의 답변을 입력받는다.
    resp = int(input())

    if resp == 1:
        break

arr = list(range(1, 10001))
random.shuffle(arr)

for b in arr:
    print("? B", b, flush=True)
            
    resp = int(input())
            
    if resp == 1:
        break

print("!", a + b)