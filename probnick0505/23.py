def f(n, stop):
    if n == stop: return 1
    if n > stop or n==21: return 0
    if n<stop: return f(n + 2, stop) + f(n + 3, stop) + f(n * 5, stop)
print(f(1,6)*f(6,35))
