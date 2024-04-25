from itertools import *
n = int(input())
k = int(input())
l = ''
# b = [l.join(str(x)) for x in range(1,k+1)]
print(permutations(l, n))
# проверка на одинаковых соседий
