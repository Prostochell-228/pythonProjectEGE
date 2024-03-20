for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (not (y) and (not (x) or ((not (z)) == w)) or z):
                    print(y, x, w, z)
