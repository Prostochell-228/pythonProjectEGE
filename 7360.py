from turtlpipe import *

screensize(2000,2000)
delay(0)
tracer(0)
k = 20
left(90)


up()
for i in range(10):
    right(120)
    forward(12*k)
down()
for i in range(7):
    forward(7*k)
    right(90)
for i in range(5):
    right(60)
    forward(20)
    right(30)

for x in range(-30,30):
    for y in range(-30, 30):
        goto(k*x,k*y)
        dot(3, 'red')
update