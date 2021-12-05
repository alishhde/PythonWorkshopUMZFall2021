# import turtle

# pen = turtle.Turtle()
# window = pen.getscreen()
# pen.speed(10)
# pen.shape("square")
# pen.shapesize(5)
# pen.width(5)

# def square(size):
#     for i in range(4):
#         if i == 0 :
#             pen.color("blue")
#         elif i == 1:
#             pen.color("red")
#         elif i == 2:
#             pen.color("yellow")
#         elif i == 3:
#             pen.color("green")
#         pen.fd(size)
#         pen.lt(90)
        
# for i in range(15):
#     square(100 + 5*i)
#     pen.fd(40)
#     pen.right(15)


    
# window.exitonclick()




import turtle


pen = turtle.Turtle()
wind = pen.getscreen()
pen.speed(10)
pen.shape('square')
pen.width(5)
def square(size):
    for i in range(4):
        if i == 0:
            pen.color('blue')
        if i == 1:
            pen.color('green')
        if i == 2:
            pen.color('yellow')
        if i == 3:
            pen.color('red')
            
        pen.forward(size)
        pen.left(90)

for i in range(10):
    square(100 + i * 10)
    pen.fd(40)
    pen.right(20)


wind.exitonclick()