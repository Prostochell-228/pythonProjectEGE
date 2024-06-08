f = open('day1_3_2.txt')
a = int((f.readline()))
h = []
for x in [x.split() for x in f]:
    s1 = int(x[0])
    print(s1)
