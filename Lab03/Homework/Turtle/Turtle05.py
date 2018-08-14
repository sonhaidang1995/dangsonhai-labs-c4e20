from turtle import *
def draw_star(x,y,length):
    # color('White')
    # setposition(x,y)
    penup()
    goto(x, y)
    pendown()
    color('red')
    speed(-1)
    for i in range(5):
        forward(length)
        right(144)
    mainloop()
draw_star(20,30,50)