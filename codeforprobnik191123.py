def tri(a):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r = ''
    while (a > 0):
        k = a % 3  # очередная цифра
        r = digits[k] + r  # приклеим к результату
        a = a // 3
    return str(r)
h = []

for i in range(9, 300):
    N = tri(i)
    if i % 4 == 0:
        k = N[-3] + N[-2] + N[-1]
        N = N + k
    else:
        k = tri(i // 3)
        N = N + k
    h.append([int(N, 3), i])
print(sorted(h))


