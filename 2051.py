a = 17*(16**455)+2**67-4**47+58
a = oct(a)[2:]
c = '2480'
s = 0
for i in c:
    s+=a.count(i)
print(s)
