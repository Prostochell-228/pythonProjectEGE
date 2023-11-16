f = open('4184.txt')
a = f.readline()
f = 0
for i in range(65, 91):
    a = a.replace(chr(i), "-")
for i in a:
    if i == ".":
        s += 1
