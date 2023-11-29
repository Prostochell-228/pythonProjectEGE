import itertools

i = itertools.product('КОМПЕГЭ', repeat=6, )
s = 0
for x in i:
    if x[0] in 'ОЕЭ' and x[-1] in 'ОЕЭ' and x[1] in 'КМПГ' and x[2] in 'КМПГ' and x[3] in 'КМПГ' and x[4] in 'КМПГ':
        s += 1
print(s)

f = open('139.csv')
a = [int(line) for line in f]
x = 0
h = 0
global x
global h
s = 0
for i in a:
    if i.count(max(i)) == 1 and len(set(i)) != len(i):
        for k in i:
            x = i.count(k)
            if x > 1:
                h = i.index(x)
                break
            if min(i) + max(i) > i[h] * x:
                s += 1
