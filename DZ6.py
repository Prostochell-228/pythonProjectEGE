# 3
p = int(input())
for x in range(1, p):
    for y in range(1, p):
        a = (6 * (p ** 0) + 1 * (p ** 1) + x * (p ** 2) + 5 * (p ** 3))
        b = (5 * (p ** 0) + x * (p ** 1) + x * (p ** 2) + x * (p ** 3))
        c = (y * (p ** 0) + y * (p ** 1) + 5 * (p ** 2) + 1 * (p ** 3) + 1 * (p ** 3))
        if a + b == c:
            print((y * (p ** 0) + x * (p ** 1) + y * (p ** 2)))
            break
#4 Я вообще не понял как решать.1) 37 система счисления 2) Делимость в этой же системе 3) Не хватает алфавита для обработки. Необходимо посетить консультацию тк. вообще непонятны боле менее сложные задачки по этой теме.
