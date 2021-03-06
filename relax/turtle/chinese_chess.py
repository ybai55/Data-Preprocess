import turtle
import os


class ChineseChess:
    UP_X = -226.5
    UP_Y = 255.5
    CUR_PIECE = None
    IS_PIECE_UP = False
    currentDir = os.path.abspath(os.path.curdir)
    turtle.mode('logo')
    turtle.hideturtle()
    turtle.TurtleScreen._RUNNING = True

    PIECES = {1: {"name": "黑将", "row": 1, "col": 5, "bg": "./res/BK.gif"},
              2: {"name": "黑士左", "row": 1, "col": 4, "bg": "./res/BA.gif"},
              3: {"name": "黑士右", "row": 1, "col": 6, "bg": "./res/BA.gif"},
              4: {"name": "黑象左", "row": 1, "col": 3, "bg": "./res/BB.gif"},
              5: {"name": "黑象右", "row": 1, "col": 7, "bg": "./res/BB.gif"},
              6: {"name": "黑马左", "row": 1, "col": 2, "bg": "./res/BN.gif"},
              7: {"name": "黑马右", "row": 1, "col": 8, "bg": "./res/BN.gif"},
              8: {"name": "黑车左", "row": 1, "col": 1, "bg": "./res/BR.gif"},
              9: {"name": "黑车右", "row": 1, "col": 9, "bg": "./res/BR.gif"},
              10: {"name": "黑炮左", "row": 3, "col": 2, "bg": "./res/BC.gif"},
              11: {"name": "黑炮右", "row": 3, "col": 8, "bg": "./res/BC.gif"},
              12: {"name": "黑卒1", "row": 4, "col": 1, "bg": "./res/BP.gif"},
              13: {"name": "黑卒2", "row": 4, "col": 3, "bg": "./res/BP.gif"},
              14: {"name": "黑卒3", "row": 4, "col": 5, "bg": "./res/BP.gif"},
              15: {"name": "黑卒4", "row": 4, "col": 7, "bg": "./res/BP.gif"},
              16: {"name": "黑卒5", "row": 4, "col": 9, "bg": "./res/BP.gif"},
              17: {"name": "红将", "row": 10, "col": 5, "bg": "./res/RK.gif"},
              18: {"name": "红士左", "row": 10, "col": 4, "bg": "./res/RA.gif"},
              19: {"name": "红士右", "row": 10, "col": 6, "bg": "./res/RA.gif"},
              20: {"name": "红象左", "row": 10, "col": 3, "bg": "./res/RB.gif"},
              21: {"name": "红象右", "row": 10, "col": 7, "bg": "./res/RB.gif"},
              22: {"name": "红马左", "row": 10, "col": 2, "bg": "./res/RN.gif"},
              23: {"name": "红马右", "row": 10, "col": 8, "bg": "./res/RN.gif"},
              24: {"name": "红车左", "row": 10, "col": 1, "bg": "./res/RR.gif"},
              25: {"name": "红车右", "row": 10, "col": 9, "bg": "./res/RR.gif"},
              26: {"name": "红炮左", "row": 8, "col": 2, "bg": "./res/RC.gif"},
              27: {"name": "红炮右", "row": 8, "col": 8, "bg": "./res/RC.gif"},
              28: {"name": "红兵1", "row": 7, "col": 1, "bg": "./res/RP.gif"},
              29: {"name": "红兵2", "row": 7, "col": 3, "bg": "./res/RP.gif"},
              30: {"name": "红兵3", "row": 7, "col": 5, "bg": "./res/RP.gif"},
              31: {"name": "红兵4", "row": 7, "col": 7, "bg": "./res/RP.gif"},
              32: {"name": "红兵5", "row": 7, "col": 9, "bg": "./res/RP.gif"}}
    BOARD_COR = {}
    SCREEN = None

    def __init__(self):
        self.mainloop()

    def cvt_cor(self, x, y):
        """
        covert upper left as (0, 0) to original turtle cor. vice versa
        """
        return x + self.UP_X, self.UP_Y - y

    def cor_2_ncor(self, x, y):
        """
        covert upper left as (0, 0) to original turtle cor. vice versa
        """
        return x - self.UP_X, self.UP_Y - y

    def cor_to_symbol(self, x, y):
        """
        x, y 原始坐标
        转换为在哪个格子内
        """
        # move x, y to the cell right, down of current coordinate by x + half cell and y - half cell.
        x = x + 28.5
        y = y - 28.5
        # convert current coordinate to upper left as (0, 0) coordinates.
        x, y = self.cor_2_ncor(x, y)
        # add one to make it upper left pint as (1, 1).
        row = int(y // 57 + 1)
        col = int(x // 57 + 1)
        board_cor = str(row)+','+str(col)
        print("----当前旗子位置----")
        print('%s' % board_cor)
        # TODO：要做棋盘更新。把旧的旗子去掉。
        # TODO：要做子的限定。限定子不能走的位置。
        if self.IS_PIECE_UP is True:
            print("piece up is true")
            if self.CUR_PIECE is not None:
                self.BOARD_COR[str(row) + ',' + str(col)] = self.CUR_PIECE
                # Remove last piece
                x_col, y_row = self.cvt_cor((self.CUR_PIECE['col'] - 1) * 57, (self.CUR_PIECE['row'] - 1) * 57)
                for item in self.SCREEN.turtles():
                    if item.xcor() == x_col and item.ycor() == y_row:
                        print("clear a turtle")
                        # item.hideturtle()
                        key = str(self.CUR_PIECE['row']) + ',' + str(self.CUR_PIECE['col'])
                        self.BOARD_COR.pop(key)

                        new_x, new_y = self.cvt_cor((col - 1) * 57, (row - 1) * 57)
                        item.penup()
                        item.setpos(new_x, new_y)
                        row = int(y // 57 + 1)
                        col = int(x // 57 + 1)
                        new_board_cor = str(row) + ',' + str(col)
                        self.BOARD_COR[new_board_cor] = self.CUR_PIECE
                        self.BOARD_COR[new_board_cor]['row'] = row
                        self.BOARD_COR[new_board_cor]['col'] = col
                        print("----新旗子位置----")
                        print('%s \n\n' % new_board_cor)

                self.SCREEN.update()
                self.CUR_PIECE = None
                self.IS_PIECE_UP = False
        else:
            if board_cor in self.BOARD_COR:
                if self.CUR_PIECE is None:
                    self.CUR_PIECE = self.BOARD_COR[str(row) + ',' + str(col)]
                    print(self.CUR_PIECE['name'])
                    self.IS_PIECE_UP = True

    def print_cor(self, x, y):
        self.cor_to_symbol(x, y)

    def board(self):
        screen = turtle.Screen()
        screen.tracer(0, 0)
        screen.screensize(600, 600)
        screen.setup(800, 800, 0, 0)
        screen.bgcolor('#D6C49E')
        screen.bgpic('./res/BOARD.gif')
        screen.onscreenclick(self.print_cor)
        return screen

    def fxn(self, x, y):
        # stop backtracking
        turtle.ondrag(None)

        # move the turtle's angle and direction
        # towards x and y
        turtle.setheading(turtle.towards(x, y))

        # go to x, y
        turtle.goto(x, y)

        # call again
        turtle.ondrag(self.fxn)

    def chessman(self, screen):
        for item in self.PIECES:
            # 列对应x坐标变化， 行对应y坐标变化
            col = self.PIECES[item]['col'] - 1
            row = self.PIECES[item]['row'] - 1
            x, y = self.cvt_cor(col * 57, row * 57)
            piece = turtle.Turtle()
            screen.addshape(self.PIECES[item]['bg'])
            piece.shape(self.PIECES[item]['bg'])
            piece.penup()
            piece.setpos(x, y)
            self.BOARD_COR[str(row+1)+','+str(col+1)] = self.PIECES[item]
        screen.update()
        print(self.BOARD_COR)

    def mainloop(self):
        self.SCREEN = self.board()
        self.chessman(self.SCREEN)
        turtle.mainloop()


cc = ChineseChess()