from turtle import *
t=Turtle()
sc=Screen()
def movefd():
    t.fd(100)

def movebd():
    t.backward(100)

def moveup():
    t.left(90)
    t.fd(100)


def movedown():
    t.right(90)
    t.fd(100)
sc.listen()
sc.onkey(movebd,'a')
sc.onkey(movefd,'Up')
sc.onkey(moveup,'Left')
sc.onkey(movedown,'Right')

done()