a = []
b = []
c = []
s = 0
def test(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
def sum_of_digits(n):
    return sum([int(digit) for digit in str(n)])
def find(n):
    original_sum = sum_of_digits(n)

    while True:
        n += 1

        next_sum = sum_of_digits(n)

        if next_sum == original_sum:
            return n
#1
for i in a:
    i = str(i).split()
    for j in i:
        b.append(int(j))
    c.append(sum(b))
print(c.count(max(c)))
#2
for i in range(len(a)-1):
    if test(a[i]) and test(a[i+1]):
        s+=1
print(s)
#3
number = 0
next = find(number)
print(next)


