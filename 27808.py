def F(x, hod):
    if hod == 2 and x >= 41: return True
    if hod < 2 and x < 41: return F(x + 1, hod + 1) or F(x + 3, hod + 1) or F(x * 2, hod + 1)
    return False


for s in range(1, 40 + 1):
    if F(s, 0):
        print(s)
        break
