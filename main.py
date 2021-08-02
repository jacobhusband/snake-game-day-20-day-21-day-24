from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

SCREEN_FRAME = 300

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    score.update_scoreboard()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.increase_length()

    # Detect collision with the wall
    if snake.head.xcor() > SCREEN_FRAME or snake.head.xcor() < -SCREEN_FRAME or \
            snake.head.ycor() > SCREEN_FRAME or snake.head.ycor() < -SCREEN_FRAME:
        score.reset()
        snake.reset()

    # Detect collision with the tail
    # If the head touches any segment of the tail then trigger the game over sequence.
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
