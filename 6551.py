import functools
@functools.lru_cache()
def F():
    print()

f = open('6551a.txt')
d = f.readline()
a = [int(x.replace('\n', '')) for x in f]
