f = open('3358.txt')
g = f.readline()
s = 0
gg= []
for i in range(1, len(g)):
    s+=1
    if g[i-1]<=g[i]:
        gg.append(s)
        s = 0
print(max(gg))