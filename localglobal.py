x=500 #global variable
def test():
    x=10 #local variable
    global y
    y=600
    print(" ander wala x=",x)
    a=globals()['x']
    print(" bhar wala x=", a)

test()
print(" bahar wala x=",x)
print(y)