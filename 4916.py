import re
with open('4917.txt') as f:
    a = f.read().strip()
a = a.replace("A", "ABA")
print(len(re.findall(r'A[^A^B]{,10}A', a)))