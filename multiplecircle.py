from turtle import *
t=Turtle()
c=['red','green','blue']
t.speed(0)
for i in range(100):
    t.pencolor(c[i%3])
    t.pensize(i+1)
    t.circle(50)
    t.penup()
    t.left(90)
    t.fd(5+i)
    t.pendown()
done()