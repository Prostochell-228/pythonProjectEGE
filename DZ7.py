import re

f = open('DZ17.txt')
s = f.readline()
print(s.count('()'))

f = open('DZ27.txt')
s = f.readline()
print(s.count('TIK'))
print(s.count('TOK'))

f = open('DZ37.txt')
s = f.readline()
s = s.replace("КОТ", '-')
for i in 'КОТ':
    s = s.replace(i, '  ')
s = s.split(' ')
print(len(max(s)))

f = open('DZ47.txt')
s = f.readline()
matches = re.findall(r'A[BCDEF]{5,8}F', s)
count = len(matches)
print(count)

f = open('DZ57.txt')
s = f.readline()
matches = re.findall(r'[XY]*[YX]', s)
count = len(matches)
print(count)