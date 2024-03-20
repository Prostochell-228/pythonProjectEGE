for x in range(80):
    for y in range(80):
        for z in range(80):
            for w in range(80):
                if 2 * x + z == 2 * y + w and y + 2 * w == 47 and 2 * z + x == 68:
                    print(x, y, z, w, 2 * z + x)
s = '0' + '1221' * 7 + '12' * 20 + '0'
while '00' in s:
    s = s.replace('011', '20', 1)
    s = s.replace('022', '10', 1)
    s = s.replace('02', '110', 1)
    s = s.replace('01', '220', 1)
print(s.count('1'), s.count('2'))
