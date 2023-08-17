from turtle import *
import time
screen=Screen()
t=Turtle()
screen.setup(420,320)
#screen.bgpic('bg.gif')
t.shape('turtle')
t.color('darkgoldenrod','black')
s=10
t.pu()
t.setpos(30,30)
t.pd()


for i in range(28):
        s=s+2
        t.stamp()
        t.pu()
        t.forward(s)
        t.pd()
        t.right(25)
        time.sleep(0.25)      #activated with a break of a 1/4th of a second