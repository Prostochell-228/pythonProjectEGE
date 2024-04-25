def DD(l):
    h = []
    for i in range(2, round(l ** 0.5) + 1):
        if l % i == 0:
            h.append(i)
            h.append((l // i))
    return h

def chk(n, h):
    for i in h:
        if n%i==0:
            return False
    return True

for n in range(4, 100):
    st = '3' + '7' * n
    while ('37' in st) or ('577' in st) or ('777' in st):
        if '37' in st:
            st = st.replace('37', '7')
        if '577' in st:
            st = st.replace('577', '73')
        if '777' in st:
            st = st.replace('777', '5')
    l = str(sum(map(int, st)))
    if len(l) == 2:
        h  = (DD(int(l)))
        if chk(n, h):
            print(l,n)
