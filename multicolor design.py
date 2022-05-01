import turtle as t
colors = ['pink','purple','blue','green','orange','yellow']
t.pen()
t.bgcolor('black')
t.speed(0)
for x in range(1,200):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)