for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (not ((not (w) or z) == y) or x):
                    print(y, w, z, x)
