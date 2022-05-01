import turtle
t = turtle.Turtle()
t.color("black")
colors = ['yellow','red','pink','cyan','light green','blue']
t.speed(1)
t.pen()
for x in range(120):
    t.pencolor(colors[x%6])
    t.circle(190-x/2,90)
    t.lt(90)
    t.circle(190-x/3,90)
    t.lt(60)