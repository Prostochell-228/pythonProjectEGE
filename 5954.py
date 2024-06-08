from turtle import *

delay(0)
tracer(0)
k = 15
left(90)

for i in range(2):
    forward(10*k)
    right(90)
    forward(4*k)
    right(90)
up()
forward(3*k)
right(90)
forward(6*k)
left(90)
down()
for i in range(2):
    forward(8*k)
    right(90)
    forward(6*k)
    right(90)
up()
for x in range(-15,15):
    for y in range(-15, 15):
        goto(k*x,k*y)
        dot(3, 'red')
done()