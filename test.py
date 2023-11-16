def convert_to(number, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result
for i in range(4, 37):
    print(convert_to(381, i), i)