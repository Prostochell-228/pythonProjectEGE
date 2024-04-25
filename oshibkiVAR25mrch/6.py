from turtle import *

tracer(0)
delay(0)
k = 15
left(90)

for i in range(3):
    fd(4*k)
    left(270)
    fd(7*k)
    right(90)
left(315)
for i in range(4):
    fd(7*k)
    right(90)
    fd(4*k)
    left(270)
up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(k*x,k*y)
        dot(3, 'red')
done()