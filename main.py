a = [222,222.24,222, 222.24, 23,24,25]


#def pps(a):
#    for i in range(2, a ** (0.5)):
#        if a % i:,
#            return False
#    return True
#
#
#s = 0
#for i in a:
#    if i % 5 == 0:
#        s += 1
#
#ss = 0
#for i in a:
#    if pps(i) and i > ss:
#        ss = i
#aa  = a.copy()
#sss = 0
#for i in a:
#    b = str(i)
#    b.split()
#    for j in b:
#        if j in "24680":
#            sss += 1
#    if sss > 2:
#        aa.remove(i)
#    sss = 0
#print(aa)
g=[]
aa  = a.copy()
sss = 0
for i in a:
    b = str(i)
    b.split()
    for j in b:
        if j in "1234567890":
            sss += int(j)
    g.append([sss,i])
    sss = 0
g.sort()
a.clear()
for i in g:
    a.append(i[1])
print(list(reversed(a)))