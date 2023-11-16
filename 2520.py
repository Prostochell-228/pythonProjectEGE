f = open('2520.txt')
a = f.readline()
b = 'eyuioa'.upper()
for i in b:
    a = a.replace(i, ' ')
a = a.split(' ')
h = []
for i in a:
    h.append(len(i))
print(max(h))