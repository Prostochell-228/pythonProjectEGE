f = open('9552.txt')
a = f.readline()
s = 0
a = a.replace("CSGO", "----")
a = a.replace("PC", "--")
for i in range(65, 91):
    a = a.replace(chr(i), " ")
a = a.split(' ')
print(len(max(a)))
