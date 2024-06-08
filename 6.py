from turtle import *
screensize(10000,10000)
tracer(0)
delay(0)
k = 15
left(90)



for i in range(3):
    down()
    for i in range(2):
        fd(10*k)
        right(90)
        fd(10*k)
        right(90)
    up()
    fd(10*k)
    right(90)
    fd(5*k)
    left(90)

for x in range(-30,30):
    for y in range(-30, 30):
        goto(k*x,k*y)
        dot(3, 'red')
done()