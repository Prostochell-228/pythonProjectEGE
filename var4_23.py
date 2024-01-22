import functools
@functools.lru_cache()
def F(n,stop,k):
    if n==stop:
        return 1
    if n>stop:return 0
    if n<stop:return F(n+2,stop, k+n+2)+F(n*3,stop,k+(n*2))+F(n*4,stop,k+(n*2))
print(F(1,600,1))