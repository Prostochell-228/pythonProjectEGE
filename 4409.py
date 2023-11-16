import re

f = open('4409.txt')
s = f.readline()
matches = re.findall(r'CB[^ABF]BC', s)
count = len(matches)
ls = {}
for match in matches:
    l = match[2]
    if l in ls:
        ls[l] += 1
    else:
        ls[l] = 1

most = max(ls, key=ls.get)
print(count, most)
