ll = []
for i in range(100,201):
    b = list(map(str,str(i)))
    b = sorted(b)
    h = b[0]+b[1]
    j = b[2]+b[1]
    c = int(j)-int(h)
    if c == 30:
        ll.append([h, j])
print(len(ll))



