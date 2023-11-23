f = open("10108.txt")
k = f.readline()
a = f.readline()
h = [int(line) for line in f]
print(k)
print(a)
print("-----------")
print(h[0])
for i in range(0, (len(h) - 2 * k - 1)):
   print()