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
    # TODO: use loop
    screen.addshape('BA', './res/BA.gif')
    screen.addshape('BB', './res/BB.gif')
    screen.addshape('BC', './res/BC.gif')

    screen.addshape('./res/BK.gif')
    print(screen.getshapes())
    BK = turtle.Turtle()
    BK.shape('./res/BK.gif')
    BK.penup()
    BK.setpos(0, 256)
    BK.ondrag(fxn)


    screen.addshape('BN', './res/BN.gif')
    screen.addshape('BP', './res/BP.gif')
    screen.addshape('BR', './res/BR.gif')

    screen.addshape('RA', './res/RA.gif')
    screen.addshape('RB', './res/RB.gif')
    screen.addshape('RC', './res/RC.gif')
    screen.addshape('RK', './res/RK.gif')
    screen.addshape('RN', './res/RN.gif')
    screen.addshape('RP', './res/RP.gif')
    screen.addshape('RR', './res/RR.gif')

    screen.update()
    print(screen.getshapes())




screen = board()
chessman(screen)



turtle.mainloop()
