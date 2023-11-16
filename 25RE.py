import re

for i in range(1923, 10 ** 8, 1923):
    a = re.findall(r'^1\d*2\d\d76$', str(i))
    if a:
        if len(a) == 1:
            print(i, i//1923)
