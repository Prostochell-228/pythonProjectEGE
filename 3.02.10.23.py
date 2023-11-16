def test3(c):
    s = str(c)
    s = list(s)
    for i in range(1,len(s)):
        if s[i]<s[i-1]:
            return False
    return True
s = []
for i in range(1395, 22718):
    if test3(i):
        s.append(i)
print(sum(s))
