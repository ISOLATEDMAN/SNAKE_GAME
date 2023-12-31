from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.grow()

    def create_snake(self):
        for position in starting_position:
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.segments.append(new_snake)

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def grow(self):
            new_snake1 = Turtle(shape="square")
            new_snake1.color("white")
            new_snake1.penup()
            self.segments.append(new_snake1)


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(move_distance)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

        
    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)
