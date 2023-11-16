from itertools import product

a = list(product(sorted("компьютер"), repeat=5))
print(a.index(('ю','ю','ю','к','к'))+1)




