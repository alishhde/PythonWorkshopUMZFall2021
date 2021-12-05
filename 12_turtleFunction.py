

def draw_poly(p, num, size):
    angle = 360 / num
    
    for i in range(num):
        p.fd(size)
        p.lt(angle)


import turtle

pen = turtle.Turtle()
window = pen.getscreen()

draw_poly(pen, 8, 50)

window.exitonclick()

