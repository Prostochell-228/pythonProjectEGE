for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if y and not (y or z) or not (not (y) or z) and (not (w) or x):
                    print(z, x, w, y)
