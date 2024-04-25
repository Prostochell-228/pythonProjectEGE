h = []
for i in range(10**10,10**11,2023):
    h.append([sum(list(map(int, str(i)))), i])
    print(i)
print(sorted(h)[::-1])
