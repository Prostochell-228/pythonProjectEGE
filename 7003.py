h = 1
for x in '0123456789AB':
    for y in '0123456789ABCDEFGH':
        j12 = '67' + x + x + '3'
        j14 = '2' + x + '9' + x
        j15 = '44' + x + x + '3'
        j18 = '2' + x + y + '7'
        a = int(j12, 12) + int(j14, 14) + int(j15, 15) - int(j18, 18)
        if a > 0 and a % 77 == 0:
            h *= int(x, 12)
            h *= int(y, 18)
print(h)
