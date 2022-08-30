from turtle import Turtle 

class Snake():
    
    def __init__(self):
        segments = []
        
        for t in range(0,3):
            new_segment = Turtle(shape = "square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setx(t*-20)
            segments.append(new_segment)
            
    def move(self):
        for seg_num in range(len(self)-1, 0, -1):
            next_x = self[seg_num - 1].xcor()
            next_y = self[seg_num - 1].ycor()
            self[seg_num].goto(next_x, next_y)