h = []
for x in '0123456789ABCDEF':
    for y in '0123456789ABCDEF':
        j = '27A' + x + '23'
        jj = '8' + y + 'E5D2'
        if (int(j, 16)+int(jj, 16)) % 5 == 0 :
            h.append([int(x, 16) + int(y, 16),x,y])
print(max(h))
