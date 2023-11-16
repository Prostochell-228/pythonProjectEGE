f = open('3438.txt')
g = f.readline()
h = []
for i in range(5):
    for j in range(i, len(g)-4, 5):
            if g[j]==g[j+4] and g[j+1]==g[j+3]:
                h.append(g[j]+g[j+1]+g[j+2]+g[j+3]+g[j+4])
print(len(h))