f = open('3347.txt')
g = ''
g = f.readline()
a = ['F','A','I','L']
for i in a:
    gg = g
    b = a.copy()
    b.remove(i)
    for j in b:
        gg = gg.replace(j," ")
    gg = gg.split(" ")
    print(len(max(gg)))
