import sys
input = sys.stdin.readline

def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

for i in range(3, 0, -1):
    n = input().strip()
    if n.isdigit():
        fizzbuzz(int(n)+i)
        break