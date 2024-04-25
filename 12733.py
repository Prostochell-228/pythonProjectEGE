def F(A):
    for x in range(2000):
        for y in range(2000):
            if not((x>56) or (y>=x) or ((3*x-y)<A)):
                return False
    return True
for A in range(1000):
    if F(A):
        print(A)
        break