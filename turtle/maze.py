import turtle

win = turtle.Screen()
win.bgcolor("light blue")
win.title("Maze - made by turtle")

distance = 15
angle = 90

pen = turtle.Turtle()

for i in range(0, 1240):
    pen.forward(distance)
    pen.right(angle)
    distance = distance + 15    

turtle.done()