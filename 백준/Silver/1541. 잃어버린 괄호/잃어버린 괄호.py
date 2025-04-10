import re

exp = input().strip()

exp = re.sub('-', ')-(', exp)
exp = re.sub(r'\b0+(\d)', r'\1', exp)

print(eval('(' + exp + ')'))