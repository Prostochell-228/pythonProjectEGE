nums = [1, 20, 30, 45, 67, 89, 100, 101, 200]
alls = [1, 'a', 'a', 'a', 67, 89, 100, 101, 200]
s = ''
# 1
for i in nums:
    if i in range(10, 100):
        s += '1'
    else:
        s += '0'
s = (s.replace('0', ' ')).split(' ')
print(len(max(s)))
s = ''
# 2
for i in alls:
    i = str(i)
    if i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъёфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
        s += i
    else:
        s += '_'
s = (s.replace('_', ' ')).split(' ')
print(len(max(s)))
# 3
ct = {}
s = 0
for i in nums:
    x = i % 7
    if x == 0:
        s += ct.get(0, 0)
    else:
        s += ct.get(7 - x, 0)
    ct[x] = ct.get(x, 0) + 1
print(s)