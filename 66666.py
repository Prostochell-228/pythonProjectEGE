dword_40C0 = []
j = None
i = None

for i in range(256):
    v3 = i
    for j in range(8):
        if ((v3 & 1) != 0):
            v3 = (v3 >> 1) ^ 0xEDB88320
        else:
            v3 >>= 1
    dword_40C0.append(v3)
#print(dword_40C0)

def CheckSimbol(x):
    x = ord(x)
    a3 = 0xFFFFFFFF
    for i in range(2):
        x += 1
        a3 = (a3 >> 8) ^ dword_40C0[a3 ^ x]
    return a3

letters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

for letter in letters:
    try:
        if CheckSimbol(letter) == 3989823987:
            print(letter)
            break
    except:
        pass