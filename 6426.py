import fnmatch
def test(m):
    h=[]
    for i in range(2,round(m**0.5)+1):
        if m%i==0:
            h.append([i,m//i])
    if len(h)==1:
        return h
    else:
        return []
for i in range(1230405, 10 ** 8 + 1):
    if fnmatch.fnmatch(str(i), '123*4?5') == True:
        if True:
            print