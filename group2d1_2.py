for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not (x) or (z == w)) or not (not (y) or w)):
                    print(y, x, w, z)
