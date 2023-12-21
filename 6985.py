for i in range(2,200):
    N = bin(i)[2:]

    if  N[-1]==N[-2]:
        N =N+'0'
    else:
        N = N+'1'
    if  N[-1]==N[-2]:
        N =N+'0'
    else:
        N = N+'1'

    if int(N,2)>93:
        print(i)