with open('24_9791.txt') as f:
    a = f.readline()
for i in range(71,91):
    a = a.replace(chr(i), " ")
a = a.split(" ")
b = []
for i in a:
    b.append(len(i))
print(max(b))