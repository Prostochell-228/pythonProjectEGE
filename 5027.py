s = 0
def divisors(n):
    count = []
    global s
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 != 0:
                count.append(i)
            if (n // i) % 2 != 0 and (n // i)!=i:
                count.append((n // i))
    if len(set(count))>100:
        s = max(count)
        return True
    else:
        return  False

a = []
o = 7*13*17*23*29
for i in range(o,2000000001,o):
    if i%3!=0 and i%5!=0 and i>=1000000000 and i%10==8 and divisors(i):
        a.append([i,s])
print(sorted(a))