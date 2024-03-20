f = open('7267.txt')
a = [int(x.replace('\n','')) for x in f.readlines()]
hh = min(a)
k = []
for i in range(len(a)-1):
    if a[i]%117==hh or a[i+1]%117==hh:
        k.append(a[i]+a[i+1])
print(len(k), max(k))