a = []
b = []
for line in open(file="17_9786.txt"):
    line  = line.replace("\n", "")
    a.append(line)
for i in a:
    if i.zfill(3)[2:]=="25":
        b.append(int(i))
for i in range(len(a)-2):
    print(1)