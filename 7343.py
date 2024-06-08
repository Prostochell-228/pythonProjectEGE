f = [x for x in open('7354.csv')]
s = 0
for line in f:
    m = sorted([int(x) for x in line.split()])
    if len(m)-len(set(m))==1 and ((m[0]+m[5])/2)>((m[1]+m[2]+m[3]+m[4])/4):
        s+=1
print(s)

