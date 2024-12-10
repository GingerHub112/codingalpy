import turtle

turtle.Screen().bgcolor("orange")

pen = turtle.Turtle()

pen.up()
pen.goto(10,10)
pen.down()

for i in range(0, 90):
    pen.forward(1)
    pen.right(4)

pen.up()
pen.goto(-23, -23)
pen.down()

for j in range(0, 4):
    pen.forward(190)
    pen.right(90)

pen.up()
pen.goto(143, 134)
pen.down()

for k in range(0, 3):
    pen.forward(76)
    pen.left(360/3)

pen.up()
pen.goto(-143, 134)
pen.down()

for l in range(0, 6):
    pen.forward(76)
    pen.right(360/6)

turtle.done()