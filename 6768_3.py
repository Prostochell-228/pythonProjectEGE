def F(x, hod):
    if (hod == 4 or hod == 2) and x >= 59: return True
    if hod < 4 and x < 59:
        a = F(x + 1, hod + 1), F(x + 4, hod + 1), F(x * 3, hod + 1)
        if hod % 2 == 0:
            return all(a)
        if hod % 2 != 0:
            return any(a)
    return False


for s in range(1, 58 + 1):
    if F(s, 0):
        print(s)
