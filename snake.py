from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_blocks = []
        for _ in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            self.snake_blocks.append(t)

        self.snake_blocks[1].goto(x=-20, y=0)
        self.snake_blocks[2].goto(x=-40, y=0)

        self.head = self.snake_blocks[0]

    #  Logic: for moving snake and update it perfectly so no inconsistency between program
    # we used: last piece of snake move to second last piece
    # then 2nd last move to 3rd last, etc. etc.
    # until the 2nd piece will move to first one
    # and first one will move to new position
    # This will help and follow the instruction of first piece of snake
    # wee just have to move 1st piece of snake and rest piece will follow along

    def move(self):
        for piece in range(len(self.snake_blocks) - 1, 0, -1):
            # we need n-1 snake_piece coordinates
            x_cord = self.snake_blocks[piece - 1].xcor()
            y_cord = self.snake_blocks[piece - 1].ycor()

            self.snake_blocks[piece].goto(x_cord, y_cord)  # moving nth piece to n-1 piece

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            # this will control if snake going one direction
            # it will not be allowed to go opposite direction
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

