from math import *
a = int(input("enter first number"))
b = int(input("enter Second number"))
c = int(input("enter third number"))

d=b*b-4*a*c
print(d)
if d==0:
    print("roots are real and equal")
    x1=x2=-b/(2*a)
    print("X1=",x1,"x2=",x2)
elif d>0:
    print("roots are real and unequal")
    x1 = (-b+sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("X1=", x1, "x2=", x2)
else:
    print("roots are imaginary")