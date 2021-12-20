from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment_size = 20
        self.starting_length = 3
        self.starting_positions = []
        for i in range(self.starting_length):
            self.starting_positions.append((-i * self.segment_size, 0))
        self.segments = []
        self.to_grow = 0
        self.head = None
        self.init_snake()

    def init_snake(self):
        for position in self.starting_positions:
            self.init_segment(position)
        self.head = self.segments[0]

    def reset_snake(self):
        for seg in self.segments:
            seg.ht()
        self.segments.clear()
        self.init_snake()

    def init_segment(self, position):
        t = Turtle()
        t.penup()
        t.color("white")
        t.shape("square")
        t.pensize(self.segment_size)
        t.goto(position)
        self.segments.append(t)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            pos = (self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
            self.segments[i].goto(pos)
        if self.to_grow > 0:
            pos = (self.segments[-1].xcor(), self.segments[-1].ycor())
            self.init_segment(pos)
            self.to_grow -= 1
        self.head.forward(self.segment_size)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
