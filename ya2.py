for x in range(2):
    for y in range(2):
        for w in range(2):
            if ((not (x) or y) and (w or not (w))):
                print(w, x, y)
