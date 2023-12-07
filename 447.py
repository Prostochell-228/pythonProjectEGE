def F(x, stop):
    if x==stop: return 1
    if x>stop: return 0
    if x<stop: return F(x+1, stop)+F(x+2,stop)+F(x*3,stop)
print(F(2,8)*F(8,10)*F(10,12))