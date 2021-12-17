from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
TRAVEL_DISTANCE = 20
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_block(position)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_position = self.snake[i - 1].position()
            self.snake[i].goto(new_position[0], new_position[1])
        self.head.forward(TRAVEL_DISTANCE)

    def add_block(self, position):
        snake_block = Turtle(shape="square")
        snake_block.color("green", "green")
        snake_block.penup()
        snake_block.goto(position)
        self.snake.append(snake_block)

    def extend(self):
        self.add_block(self.snake[-1].position())
