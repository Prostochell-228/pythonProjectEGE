def test(n):
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def F1(n):
    if n < 2:
        return n
    else:
        if n % 2 == 0:
            return F1(n / 2) + 1
        else:
            return F1(3 * n + 1) + 1


def F2(n):
    if n == 0:
        return 1
    if n > 0:
        return 7 * (n - 1) + F2(n - 1)


def F3(n):
    if n < 10:
        return n
    else:
        return n % 10 + F3(n // 10)


def G3(n):
    if n < 10:
        return n
    else:
        return G3(F3(n))

def F00(x, stop):
    if x==stop: return 1
    if x>stop or x==10: return 0
    if x<stop: return F00(x-2, stop)+F00(x//10,stop)
print(F00(1,21))
