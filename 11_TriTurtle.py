import turtle

pen = turtle.Turtle()
window = pen.getscreen()
pen.speed(10)
pen.shape("square")
pen.shapesize(5)
pen.width(5)

def square(size):
    for i in range(4):
        if i == 0 :
            pen.color("blue")
        elif i == 1:
            pen.color("red")
        elif i == 2:
            pen.color("yellow")
        elif i == 3:
            pen.color("green")
        pen.fd(size)
        pen.lt(90)
        
for i in range(15):
    square(100 + 5*i)
    pen.fd(40)
    pen.right(15)


    
window.exitonclick()