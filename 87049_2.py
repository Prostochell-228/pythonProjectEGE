for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x or y) == (not(y) or z)) or w):
                    print(x,z,w,y)