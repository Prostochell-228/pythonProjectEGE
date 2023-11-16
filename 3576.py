x = 5 * 216**3031 + 4 * 36**3042 - 3 * 6**3053 - 3064
res =[]
while x>0:
    res.append(x%6)
    x = x//6
print(sum(res))