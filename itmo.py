from functools import lru_cache

@lru_cache(maxsize=None)
def binary_len(n):
   return len(bin(n)[2:])

def find_number(n):
   count = 0
   i = 1
   while count < n:
       if len(str(i)) * 3 == binary_len(i):
           count += 1
       i += 1
   return i - 1
print(find_number(10**8 - 58))