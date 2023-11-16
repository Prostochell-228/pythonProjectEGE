n = int(input())
def geb(n):
     g = []
     while n>=3:
          t = n%3
          n  =n//3
          g.append(str(t))
     g.append(str(n))
     return ''.join(g[::-1])
print(geb(n))
