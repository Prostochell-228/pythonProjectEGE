
def divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
            if (n // i) % 2 == 0 and (n // i)!=i:
                count += 1
    return count

a = []

for i in range(2,10**6+1,2):
    pp = divisors(75000000 + i)
    if pp%2!=0:
        a.append([i, pp])
    if len(a)==5:
        break
print(sorted(a))