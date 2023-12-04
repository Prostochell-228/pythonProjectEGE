# 1
def per(n, i):
    a = '0123456789ABCDEFG'
    s = ''
    while n > 0:
        res = a[n % i] + s
        n = n // i
    return s


# 2
def kr(x, y):
    j = min(x, y)
    while True:
        if j % x == 0 and j % y == 0:
            return j
        j+=min(x,y)
#3
def bs(a):
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a