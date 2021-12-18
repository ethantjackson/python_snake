import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")

game_running = True

while game_running:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.head.distance(food) < 17:
        food.respawn()
        scoreboard.increment_score()
        snake.to_grow += 1
    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
        scoreboard.game_over()
        game_running = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_running = False

screen.exitonclick()
