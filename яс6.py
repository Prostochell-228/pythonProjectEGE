h = []
for N in range(200):
    b = bin(N)[2:]
    if len(b)%2==0:
        B = b[:(len(b)//2)] + '000' + b[(len(b)//2):]
    else:
        B = '1'+ b +'01'
    if int(B, 2)>100: print(N); break