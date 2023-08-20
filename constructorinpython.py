'''
Constructor will run automatically when the object is created
'''

class Test:
    def msg(self):
        print("I will run with the help of object")

    def __init__(self):
        self.x = 0
        self.y = 0
        print("I can run without any object")

    def getData(self,x,y):  # value initilize
        self.x = x
        self.y = y

    def add(self):  # operate
        c=self.x+self.y
        print("sum=",c)

t=Test() # constuctor tuns
t.getData(5,88)
t.add()
t.msg()

t2=Test()