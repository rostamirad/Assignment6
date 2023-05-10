import turtle

turtle.bgcolor("white")

colors = ["black", "gray"]
p = turtle.Pen()

p.shape("turtle")
p.speed(15)
p.pendown()
p. width(4)

i = 0
while i< 150:

    for j in range(len(colors)):
        p.pencolor(colors[j])
        p.forward(i+5)
        p.right(45)
        p.forward(i+5)
        p.right(90)
        p.forward(i+5)
        p.right(135)
        i+= 3

turtle.done()