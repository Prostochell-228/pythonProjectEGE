f = open('2539.txt')
a = f.readline()
a = a.replace(")"," ")
a = a.split(" ")
print(len(max(a)))