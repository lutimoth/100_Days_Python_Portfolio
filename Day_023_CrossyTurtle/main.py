import time
from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

player = Player()


screen.listen()

screen.onkey(player.forward, "w")
screen.onkey(player.backward, "s")

gaming = True

while gaming:
    time.sleep(0.1)
    screen.update()
    
    

screen.exitonclick()