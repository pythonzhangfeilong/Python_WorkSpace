import math
import turtle
x1,y1=300,0
x2,y2=300,300
x3,y3=0,300
x4,y4=0,0
turtle.showturtle()
turtle.goto(x1,y1)
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
data=math.sqrt(x1-x3)**2+(y1-y3)**2
turtle.write(data)
print(data)
