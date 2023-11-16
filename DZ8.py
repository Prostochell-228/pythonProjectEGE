import re

f = open('DZ81.txt')
s = f.readline()
s = s.replace("KOT", "-")
for i in "STOCK":
    s = s.replace(i, " ")
s = s.split()
print(len(max(s)))
f = open('DZ81.txt')
s = f.readline()
h = 0
k = 0
j = []
for i in list(s):
    h += 1
    if i == '.':
        k += 1
    if k == 7:
        j.append([h, k])
        h = 0
        k = 0
print(j)