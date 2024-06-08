for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (not (w or x or y) or ((y or z) and x or y and (w or z))):
                    print(y, x, z, w)
