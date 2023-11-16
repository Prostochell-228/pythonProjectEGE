f = open('2528.txt')
a = f.readline()
b = 'QWERTYUIOPASDFGHJKLZXCVBNM\n'
for i in b:
    a = a.replace(i, ' ')
print(sorted(a.split(' ')))