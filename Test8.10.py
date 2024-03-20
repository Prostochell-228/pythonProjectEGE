from itertools import *

m = []
for x in product('АБРИКОС', repeat=7):
    s = ''.join(x)
    if s.count('АИ') == 0 and s.count('ИА') == 0 and s.count('АО') == 0 and s.count('ОА') == 0 and s.count('ИО') == 0 and s.count('ОИ') == 0 and s.count('БР') == 0 and s.count('РБ') == 0 and s.count('БК') == 0 and s.count('КБ') == 0 and s.count('БС') == 0 and s.count('СБ') == 0 and s.count('РК') == 0 and s.count('КР') == 0 and s.count('РС') == 0 and s.count('СР') == 0 and s.count('КС') == 0 and s.count('СК') == 0:
        m.append(s)
print(len(m))
