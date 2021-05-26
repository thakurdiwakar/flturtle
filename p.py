import turtle #pip install turtle
object=turtle.Turtle()  
wn=turtle.Screen()
wn.bgcolor("White")
object.color("Red")
object.speed(-0.21)
for i in range(150):
    object.circle(i+10)
    object.left(80)
turtle.done()
 