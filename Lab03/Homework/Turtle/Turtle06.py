from turtle import *
def draw_star(x,y,length):
    # color('White')
    # setposition(x,y)
    penup()
    goto(x, y)
    pendown()
    color('blue')
    speed(-1)
    for i in range(5):
        forward(length)
        right(144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)