f = open('6903.txt')
a = f.readline()
h = []
for i in range(len(a)):
    if a[i] in '13579':
        for j in range(i+1, len(a)):
            if a[i]==a[j]:
                k = a[i:j+1]
                h.append(k)
                break
l = []
for i in h:
    if not(i.count('F')!=len(i)-2):
        l.append(len(i))
print(max(l)-2)#В ответ нужно записоть только длинну F строки



# 2667
# 2660
# 2670
