a="0123456789ABCD"
for i in a:
    x = int(int(f'753{i}2',13)+ int(f'2{i}173',13))
    if x%12==0:
        print(x//12)
        break
