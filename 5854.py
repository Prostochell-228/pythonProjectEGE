from turtle import *

tracer(0)
delay(0)
k = 15
left(90)

right(198)
for i in range(5):
    forward(10*k)
    left(144)
up()
for x in range(-15,15):
    for y in range(-15, 15):
        goto(k*x,k*y)
        dot(3, 'red')
done()