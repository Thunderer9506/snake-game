from turtle import Turtle,Screen
from snake import Snake
import time
from Food import Food
from score_board import scoreboard

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Welcome to the snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        snake.reset()
        score.reset()

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) <15:
            score.reset()
             
screen.exitonclick()