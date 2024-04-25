f = open('15333.txt')
g = open('15333.txt')
b = max([int(x) for x in f if int(x)%19==0])
a = [int(x) for x in g]
h = []
for x in range(0, len(a)-1):
    if a[x]>b or a[x+1]>b:
        h.append(a[x] + a[x+1])
print(max(h), len(h))