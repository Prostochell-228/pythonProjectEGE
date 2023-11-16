a = open('9753.txt').readline()
a = a.split("Y")
m = 0
for i in range(len(a) - 151):
    c = 'Y'.join(a[i:i+151])
    m = max((m, len(c)))
print(m)
