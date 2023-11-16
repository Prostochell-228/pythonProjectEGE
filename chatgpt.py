def count_even_divisors(n):
    count = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
            if (n // i) % 2 == 0:
                count += 1
    return count

k = 1
result = []
while len(result) < 5:
    n = 75000000 + k
    even_divisors = count_even_divisors(n)
    if even_divisors % 2 != 0:
        result.append((k, even_divisors))
    k += 1

for k, even_divisors in result:
    print(k, even_divisors)
