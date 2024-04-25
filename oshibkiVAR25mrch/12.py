# НАЧАЛО
# ПОКА нашлось (37) ИЛИ нашлось (577) ИЛИ нашлось (777)
#  ЕСЛИ нашлось (37)
#    ТО заменить (37, 7)
#  КОНЕЦ ЕСЛИ
#  ЕСЛИ нашлось (577)
#    ТО заменить (577, 73)
#  КОНЕЦ ЕСЛИ
#  ЕСЛИ нашлось (777)
#    ТО заменить (777, 5)
#  КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
def F(n):
    while '37' in n or '577' in n or '777' in n:
        if '37' in n:
            n = n.replace('37', '7')
        if '577' in n:
            n = n.replace('577', '73')
        if '777' in n:
            n = n.replace('777', '5')
    return n


h = []


def d(x):
    h = []
    for i in range(2, round(x ** 0.5) + 1):
        if x % 2 == 0:
            h.append(i)
            h.append(x // i)
    return h


for i in range(200):
    n = '3' + '7' * i
    g = sum(list(map(int, F(n))))
    h.append(g)
print((h))
