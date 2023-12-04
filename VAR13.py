import itertools
import sys
sys.setrecursionlimit(10000)
i = itertools.product('КОМПЕГЭ', repeat=6, )
s = 0
for x in i:
    if x[0] in 'ОЕЭ' and x[-1] in 'ОЕЭ' and x[1] in 'КМПГ' and x[2] in 'КМПГ' and x[3] in 'КМПГ' and x[4] in 'КМПГ':
        s += 1
print(s)

# f = open('139.csv')
# a = [int(line.replace('\n','')) for line in f]
# x = 0
# h = 0
# s = 0
# for i in a:
#    if i.count(max(i)) == 1 and len(set(i)) != len(i):
#        for k in i:
#            x = i.count(k)
#            if x > 1:
#                h = i.index(x)
#                break
#            if min(i) + max(i) > i[h] * x:
#                s += 1
a = 0
for i in "0123456789ABCDEFGHIKLMN":
    a = int("18" + i + "89957", 22) + int("80" + i + "33", 22) + int("521" + i + "6", 22)
    if a % 21 == 0:
        print(a // 21)
        break

for i in range(10, 40):
    if not (not (1) or not (i % 6 == 0)):
        print(i)


def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * F(n - 2)
print(F(2023)/F(2019))


f = open('VAR3-17.txt')
a = [int(x) for x in f]
#for i in range(len(a)-1):
#    if str(abs(a[i]))