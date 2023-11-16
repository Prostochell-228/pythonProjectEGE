import re
with open('4917.txt') as f:
    a = f.read().strip()

print(len(re.findall(r'A[^A^B]{18,}B', a)))