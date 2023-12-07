def tree(n):
    res  =''
    while n>0:
        res+=str(n%3)
        n=n//3
    return res[::-1]
def F(x, stop):
    if x == stop: return 1
    if int(x, 3) > int(stop, 3): return 0
    if int(x, 3) < int(stop, 3): return F(tree(int(x, 3) - 2), stop) + F(x[1:], stop)


print(F('3', '212'))