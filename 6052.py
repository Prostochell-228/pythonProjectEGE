
f = open('6052.txt')
a = f.readline()
s= 0
h=[]
for i in range(2, len(a)-3, 3):
    if a[i] in 'QWRTPSDFGHJKLZXCVBNM' and a[i-1] not in 'QWRTPSDFGHJKLZXCVBNM' and a[i-2] not in 'QWRTPSDFGHJKLZXCVBNM':
        s+=1
    else:
        h.append(s)
        s=0
print(max(h))
