from turtle import *

delay(0)
tracer(0)
k = 15
left(90)

for i in range(3):
    forward(4*k)
    left(270)
    forward(7*k)
    right(90)
left(315)
for i in range(4):
    forward(7*k)
    right(90)
    forward(4*k)
    left(270)

up()
for x in range(-15, 15):
    for y in range(-15, 15):
        goto(x * k, y * k)
        dot(3, 'red')
done()
