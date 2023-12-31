from turtle import Turtle,Screen
import time
from food import Food
from score import Scoreboard
from snake import Snake


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("<---- THE_SNAKE_GAME ---->")
startin_position = [(0,0),(-20,0),(-40,0),(-60,0)]
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow() 
        scoreboard.update_screen()
        scoreboard.inrcrease_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            snake.reset()

 


screen.exitonclick()