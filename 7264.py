a = 343 ** 515 - 6 * 49 ** 520 + 5 * 49 ** 510 - 3 * 7 ** 530 - 550
af = ''
while a > 0:
    af = str(a % 7) + af
    a = a // 7
print(af.count("6"))
