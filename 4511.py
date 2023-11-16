def test(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


p = [2, 1]
pp = []
s = -1
while True:
    s+=1
    p.append(p[s]+p[s+1])
    if test(p[s]+p[s+1]):
        pp.append(p[s]+p[s+1])
    if p[s]+p[s+1]>=10**9:
        break
for i in pp:
    if i in range(10**6, 10**9+1):
        print(i, p.index(i)+1)

