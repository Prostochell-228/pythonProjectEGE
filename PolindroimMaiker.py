n = int(input())


def check_pol(n):
    if len(str(n))%2==0:
        g = str(n)[:(len(str(n)) // 2)]
        f = str(n)[(len(str(n)) // 2):]
        g = ''.join(reversed(str(g)))
        if g == f:
            return True
        else:
            return False
    else:
        g = str(n)[:(len(str(n)) // 2)]
        f = str(n)[(len(str(n)) // 2):]
        f = str(f)[1:]
        g = ''.join(reversed(str(g)))
        if g == f:
            return True
        else:
            return False


def numbers_count(n):
    while True:
        n += 1
        if check_pol(n):
            break
    return n


if len(str(n)) % 2 == 0:
    g = str(n)[:(len(str(n)) // 2)]
    f = str(n)[(len(str(n)) // 2):]
    if g >= f:
        f = ''.join(reversed(str(g)))
        print(str(g) + f)
    else:
        print(numbers_count(n))
else:
    g = str(n)[:len(str(n)) // 2]
    f = str(n)[len(str(n)) // 2:]
    s = (list(str(g)[len(str(g)) // 2:]))[0]
    f = str(f)[1:]
    if g >= f:
        f = ''.join(reversed(str(g)))
        print(str(g) + s + f)
    else:
        print(numbers_count(n))
