def F(x, stop):
    if x==stop: return 1
    if x>stop or x==15: return 0
    if x<stop: return F(x+1,stop)+F(x+3,stop)
print(F(2,10)*F(10,20))