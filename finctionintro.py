
#function definition
def greet():
    print("Good morning")


greet() #function call

print("hi hello")

greet()

for i in range(5):
    greet()


def add(x,y):# here x and y is called formal argument
    c=x+y
    print("sum=",c)

add(5,6)


a=int(input("enter first number"))
b=int(input("enter second number"))
add(a,b) # here a and b is called actual argument

x=int(input("enter first number"))
y=int(input("enter second number"))
add(x,y) # here a and b is called actual argument

def returnadd(x,y):
    c=x+y
    d=x-y
    return c,d

a,b=returnadd(55,55)
print(a,b)