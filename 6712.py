from turtle import *

screensize(300000,300000)
delay(0)
tracer(0)
k = 20
left(90)



for i in range(2):
    forward(10*k)
    right(90)
    forward(18*k)
    right(90)

up()

forward(5*k)
right(90)
forward(7*k)
left(90)

down()

for i in range(2):
    forward(10*k)
    right(90)
    forward(7*k)
    right(90)

up()
for x in range(-30,30):
    for y in range(-30, 30):
        goto(k*x,k*y)
        dot(3, 'red')
done()