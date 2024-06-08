s=0
for i in [list(map(int,x.split())) for x in open('group2d4_3.csv')]:
    j = [i.count(i[0]),i.count(i[1]),i.count(i[2]),i.count(i[3]),i.count(i[4])]
    if len(i)-len(set(i))==2 and 3 in j:
        mn = min(i)
        mx = max(i)
        i.remove(mn)
        i.remove(mx)
        if (mn+mx)**2 < i[0]**2+i[1]**2+i[2]**2:
            s+=1
print(s)