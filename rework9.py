import fnmatch
f = []
def rr(n):
    h = set()
    h.add(1)
    h.add(n)
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            h.add(i)
            h.add(n//i)
    return str(sum(h))
for i in range(500000,2000000):
    d = rr(i)
    if fnmatch.fnmatch(d,'*7?'):
        print(i, d)