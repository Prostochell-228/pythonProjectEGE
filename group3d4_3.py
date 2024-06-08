f = open('group3d4_3a.txt')
a = list(map(int, (f.readline()).split()))
x = [int(x) for x in f]
y = x[::-1]
s = 0
for i in range(len(x)):
    v = a[1]-x[i]
    for j in y:
        if j>=v:
            s+=1
        else:
            break
print(s//2)
#87496 1788748
#43748 894374