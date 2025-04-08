ans = [i.upper() if i.islower() else i.lower() for i in input().strip()]

print(''.join(ans))