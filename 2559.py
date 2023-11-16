import fnmatch

f = open('test.txt')
a = [line for line in f]
C = 0
v = 0
for i in a:
    for j in i:
        if j == "Z" and C<=len(i)-4:
            if i[C + 2] == "R" and i[C + 3] == "O":
                v += 1
                break
        C += 1
    C = 0
print(v)
