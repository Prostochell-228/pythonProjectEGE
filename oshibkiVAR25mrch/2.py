for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(y) and (x == (not(w) or z)):
                    print(x,w,z,y)#Странно. но если переставить X и W то ответ так же подходит