h = []
c = 0
cc = 0
for i in open('group2d4_5.txt').readline():
    if c >= 150:
        h.append(cc)
        c = 0
        cc = 0
    if i == 'Y':
        cc += 1
        c += 1
    else:
        cc += 1
print(max(h))
