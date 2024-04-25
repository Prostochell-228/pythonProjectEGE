for x in '0123456789ABCDEFGHIJKLM':
    a = int('7'+x+'38596', 23)+int('14'+x+'36', 23)+int('61'+x+'7', 23)
    if a%22==0:
        print(a//22)
        break