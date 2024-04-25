from fnmatch import *
def F(n):
    h = []
    if n%2==0:
        h.append(n)
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                h.append(i)
            if (n // i) % 2 == 0:
                h.append((n // i))
    return h


s = 0
for i in range(65000, 10**9+1):
    if fnmatch(str(i),'6*97*5?'):
        h = F(i)

        if len(h)>=4:
            print(i, sum(h))
            s+=1
    if s==7: break
