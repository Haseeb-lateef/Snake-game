from turtle import Turtle
MOVE_FORWARD = 20
LEFT = 180
RIGHT =0
DOWN = 270
UP = 90

class Snake:

    def __init__(self,size):
        self.size = size
        self.color = "white"
        self.shape = "square"
        self.snake_segments = self.make_snake(size)
        self.head = self.snake_segments[0]






    def make_snake(self, size):
        """
        creates each segment of the snake as a turtle object stored in a list
        :param size: the size of the snake i.e how many segments
        :return: list of snake segments(turtle objects)
        """
        snake_segments = []
        x = 0
        y= 0

        for i in range(size):
            segment = self.create_segment(x,y)
            x -= 20

            snake_segments.append(segment)
        return snake_segments


    def create_segment(self,x,y):

        new_segment = Turtle(shape=self.shape)
        new_segment.penup()
        new_segment.color(self.color)
        new_segment.goto(x=x, y=y)

        return new_segment



    def expand(self):
        tail_x = self.snake_segments[-1].xcor()
        tail_y= self.snake_segments[-1].ycor()
        new_segment = self.create_segment(tail_x,tail_y)
        self.snake_segments.append(new_segment)
        self.size+=1#counter to check snake size







    def move(self):
        """
        moves the snake forward
        :return: none
        """
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            x = self.snake_segments[seg - 1].xcor()
            y = self.snake_segments[seg - 1].ycor()
            self.snake_segments[seg].goto(x, y)
        self.snake_segments[0].forward(MOVE_FORWARD)

        return None


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def right(self):
        """
        moves the snake forward
        :return: none
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



        return None

    def left(self):
        """
        moves the snake forward
        :return: none
        """
        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)



        return None

    def down(self):
        """
        moves the snake forward
        :return: none
        """
        if self.head.heading() != UP:

            self.snake_segments[0].setheading(DOWN)

        return None


    def reset_snek(self):
        # move old segments off-screen (so they disappear)
        for seg in self.snake_segments:
            seg.goto(1000, 1000)

        self.snake_segments.clear()
        self.size = 3  # or whatever starting size you want

        # rebuild snake
        self.snake_segments = self.make_snake(self.size)
        self.head = self.snake_segments[0]




