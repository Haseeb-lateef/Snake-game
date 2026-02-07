from snake import Snake
from turtle import Screen
from food import Food
from score import Scoreboard
import time


STARTING_SIZE = 3

#SCREEN STUFF
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(STARTING_SIZE)
food = Food()
scoreboard = Scoreboard()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_continue = True


while game_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.change_food_pos()
        scoreboard.update_score()
        snake.expand()
        print(snake.size)




    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) >290:
        scoreboard.reset_game()
        snake.reset_snek()


    for seg in snake.snake_segments[1:]:

        if snake.head.distance(seg) < 10:
            scoreboard.reset_game()
            snake.reset_snek()


screen.exitonclick()


