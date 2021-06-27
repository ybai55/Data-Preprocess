from turtle import Turtle, Screen

SIZE = 40

class Box(Turtle):
    def __init__(self, x=0, y=0, place_color='green'):
        super().__init__('box')

        self.speed('fastest')
        self.color(place_color)
        self.place_color = place_color
        self.has_queen = False
        self.penup()
        self.setpos(x, y)

        self.onclick(self.click_handler)

    def click_handler(self, x, y):

        print("start:", self.has_queen)

        if self.has_queen:
            self.shape('box')
        # else:
            # self.shape('turtle')
        else:
            self.shape('./res/BK.gif')

        self.has_queen = not self.has_queen
        self.onclick(self.click_handler)  # redo since self.shape() may undo this

        print("end:", self.has_queen)

    def __str__(self):
        """ Print piece details """
        return "({0}, {1}), {2}".format(self.xcor(), self.ycor(), self.place_color)

screen = Screen()
screen.register_shape('box', ((-SIZE/2, SIZE/2), (SIZE/2, SIZE/2), (SIZE/2, -SIZE/2), (-SIZE/2, -SIZE/2)))
screen.register_shape('./res/BK.gif')

tortoise = Box()

screen.mainloop()