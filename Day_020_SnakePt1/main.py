from turtle import Screen, Turtle, tracer
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake-y Snake Time")

# Turn off automatic animations
screen.tracer(0)

segments = []
for t in range(0,3):
    new_segment = Turtle(shape = "square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.setx(t*-20)
    segments.append(new_segment)

gaming = True

while gaming:
    # Keep update outside for loop so we only update when all 3 segments moved
    screen.update()
    time.sleep(0.1)
    
    # for seg in segments: This is not good
    #     seg.forward(20)  Prevents turning
    
    # Move each segment into the position of the previous segment
    # Start from tail
    for seg_num in range(len(segments)-1, 0, -1):
        next_x = segments[seg_num - 1].xcor()
        next_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(next_x, next_y)
    
    # Move the last segment (head) forward
    segments[0].forward(20)  

screen.exitonclick()