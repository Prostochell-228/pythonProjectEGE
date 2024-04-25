def F(A):
    h = []
    for i in range(2,round(A**0.5)+1):
        if A%i==0:
            if i%2!=0:
                h.append(i)
            h.append(A//i)
    return h
for i in range(18782, 18823):
    print()