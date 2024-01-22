def F(x, hod):
    if hod == 2 and x >= 68: return True
    if hod < 2 and x < 68: return F(x + 1, hod + 1) or F(x + 4, hod + 1) or F(x * 5, hod + 1)
    return False


for s in range(1, 67 + 1):
    if F(s, 0):
        print(s)
        break
