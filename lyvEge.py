a=0;b=0;s=1
#1
print((a+b)/2)

#
if (int(input())%10)%2==0:
    print("чётное")
else:
    print("нечётное")

#
print(len([x for x in range(10, 100, 2)]))

#
print(sum([x for x in range(10, 301, 10)]))

#
a = [x for x in range(a, b) if x%10==5]
for i in a:
    s*=i
print(s)




print("------------")
a=0;b=0;s=1
#2
x = str(122)
x.split()
for i in x:
    if i in "02468":
        s*=int(i)
print(s)

#
x = str(122)
x.split()
for i in x:
    if i in "02468":
        a+=1
print(a)

#
x=16
for i in range(1, round(x**0.5)+1):
    if x%i==0:
        print(i, x//i)




print("------------")
a=[];b=0;s=1
#3
def test(x):
    for i in range(2, round(x**0.5)+1):
        if x%i==0:
            return False
    return True

#
x = str(122)
x.split()
a = [x for x in range(1, int(max(x))+1)]
for i in a:
    s*=i
print(s)


#
x = 16
for i in range(1, round(x**0.5)+1):
    if x%i==0:
        if test(i):
            a.append(i)
        if test(x//i):
            a.append(x//i)
print(max(a))
