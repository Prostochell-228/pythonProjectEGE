f = open('09_9778.csv')
a = [(line.replace(";"," ")).replace("\n","") for line in f]
s = 0
def setcheker(i, st):
    g = 0
    c = 0
    for j in i:
        if j in st:
            g+=1
        if g>1:
            c=j
            g=0
    st.remove(c)
    print(st)
    if c>=(sum(st)/4):
        return True
    else:
        return  False
b = []
l = []
for i in a:
    s+=1
    i = i.split(" ")
    for g in i:
        b.append(int(g))
    if len(set(b))+1==len(b) and setcheker(b, set(b)):
        l.append(s)
    b.clear()
print(min(l))