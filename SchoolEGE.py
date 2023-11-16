from sys import setrecursionlimit

a = "1234567890abcdefghijkl"
for i in a:
    v = (int(f'18{i}89957', 22) + int(f'80{i}33', 22) + int(f'521{i}6', 22))
    if v % 21 == 0:
        print(v // 21)
        break
setrecursionlimit(2000)
def F(x):
    if x<7:
        return 7
    if x>=7:
        return x + 1 + F(x-2)
print(F(2024)-F(2020))
