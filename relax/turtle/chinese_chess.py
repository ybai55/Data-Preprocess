import turtle
import os

currentDir = os.path.abspath(os.path.curdir)
turtle.mode('logo')
turtle.hideturtle()
turtle.TurtleScreen._RUNNING = True

CUR_PIECE = None


def print_cor(x, y):
    print(x, y)


def mv_cm(tu):
    print(tu)



def board():
    screen = turtle.Screen()
    screen.tracer(0, 0)
    screen.screensize(600, 600)
    screen.setup(800, 800, 0, 0)
    screen.bgcolor('#D6C49E')
    screen.bgpic('./res/BOARD.gif')
    screen.onscreenclick(print_cor)
    return screen


def fxn(x, y):
    # stop backtracking
    turtle.ondrag(None)

    # move the turtle's angle and direction
    # towards x and y
    turtle.setheading(turtle.towards(x, y))

    # go to x, y
    turtle.goto(x, y)

    # call again
    turtle.ondrag(fxn)


def chessman(screen):
    # TODO: use loop
    # 卒
    screen.addshape('./res/BP.gif')
    for i in range(0, 10, 2):
        BA = turtle.Turtle()
        BA.shape('./res/BP.gif')
        BA.penup()
        BA.setpos(-224+i*56, 144-56)
    # 炮
    screen.addshape('./res/BC.gif')
    BA = turtle.Turtle()
    BA.shape('./res/BC.gif')
    BA.penup()
    BA.setpos(-168, 144)
    BA = turtle.Turtle()
    BA.shape('./res/BC.gif')
    BA.penup()
    BA.setpos(168, 144)
    # 车
    screen.addshape('./res/BR.gif')
    BA = turtle.Turtle()
    BA.shape('./res/BR.gif')
    BA.penup()
    BA.setpos(-224, 256)
    BA = turtle.Turtle()
    BA.shape('./res/BR.gif')
    BA.penup()
    BA.setpos(224, 256)
    # 马
    screen.addshape('./res/BN.gif')
    BA = turtle.Turtle()
    BA.shape('./res/BN.gif')
    BA.penup()
    BA.setpos(-168, 256)
    BA = turtle.Turtle()
    BA.shape('./res/BN.gif')
    BA.penup()
    BA.setpos(168, 256)
    # 象
    screen.addshape('./res/BB.gif')
    BA = turtle.Turtle()
    BA.shape('./res/BB.gif')
    BA.penup()
    BA.setpos(-112, 256)
    BA = turtle.Turtle()
    BA.shape('./res/BB.gif')
    BA.penup()
    BA.setpos(112, 256)
    # 士
    screen.addshape('./res/BA.gif')
    BA = turtle.Turtle()
    BA.shape('./res/BA.gif')
    BA.penup()
    BA.setpos(-56, 256)
    BA = turtle.Turtle()
    BA.shape('./res/BA.gif')
    BA.penup()
    BA.setpos(56, 256)
    # 将
    screen.addshape('./res/BK.gif')
    BK = turtle.Turtle()
    BK.shape('./res/BK.gif')
    BK.penup()
    BK.setpos(0, 256)

    # 兵
    screen.addshape('./res/RP.gif')
    for i in range(0, 10, 2):
        BA = turtle.Turtle()
        BA.shape('./res/RP.gif')
        BA.penup()
        BA.setpos(-224 + i * 56, 144 - 4*56)
    # 炮
    screen.addshape('./res/RC.gif')
    BA = turtle.Turtle()
    BA.shape('./res/RC.gif')
    BA.penup()
    BA.setpos(-168, 144-5*56)
    BA = turtle.Turtle()
    BA.shape('./res/RC.gif')
    BA.penup()
    BA.setpos(168, 144-5*56)
    # 车
    screen.addshape('./res/RR.gif')
    BA = turtle.Turtle()
    BA.shape('./res/RR.gif')
    BA.penup()
    BA.setpos(-224, 256-9*56)
    BA = turtle.Turtle()
    BA.shape('./res/RR.gif')
    BA.penup()
    BA.setpos(224, 256-9*56)
    # 马
    screen.addshape('./res/RN.gif')
    BA = turtle.Turtle()
    BA.shape('./res/RN.gif')
    BA.penup()
    BA.setpos(-168, 256-9*56)
    BA = turtle.Turtle()
    BA.shape('./res/RN.gif')
    BA.penup()
    BA.setpos(168, 256-9*56)
    # 象
    screen.addshape('./res/RB.gif')
    BA = turtle.Turtle()
    BA.shape('./res/RB.gif')
    BA.penup()
    BA.setpos(-112, 256-9*56)
    BA = turtle.Turtle()
    BA.shape('./res/RB.gif')
    BA.penup()
    BA.setpos(112, 256-9*56)
    # 士
    screen.addshape('./res/RA.gif')
    BA = turtle.Turtle()
    BA.shape('./res/RA.gif')
    BA.penup()
    BA.setpos(-56, 256-9*56)
    BA = turtle.Turtle()
    BA.shape('./res/RA.gif')
    BA.penup()
    BA.setpos(56, 256-9*56)
    # 将
    screen.addshape('./res/RK.gif')
    BK = turtle.Turtle()
    BK.shape('./res/RK.gif')
    BK.penup()
    BK.setpos(0, 256-9*56)

    screen.update()
    print(screen.getshapes())




screen = board()
chessman(screen)



turtle.mainloop()
