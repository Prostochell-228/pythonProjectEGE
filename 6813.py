from turtle import *

delay(0)
tracer(0)
k = 15
left(90)
for i in range(3):
    left(90)
    for j in range(4):
        fd(5 * k)
        right(90)
up()
for x in range(-15, 15):
    for y in range(-15, 15):
        goto(x * k, y * k)
        dot(3, 'red')
done()
