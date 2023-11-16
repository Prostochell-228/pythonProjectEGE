from turtle import *

left(90)
for _ in range(2):
    forward(13 * 20)
    right(90)
    forward(20*20)
    right(90)
pu()
forward(8*20)
right(90)
backward(3*20)
left(90)
for _ in range(2):
    forward(16*20)
    right(90)
    forward(8*20)
    right(90)
pu()
for x in range(50):
    for y in range(50):
        goto(x * 20, y * 20)
        dot(4)