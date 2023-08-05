from math import *
a=int(input("enter the first side of traingle"))
b=int(input("enter the second side of traingle"))
c=int(input("enter the tird side of traingle"))

s=(a+b+c)/2
print(s)
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("area=",area)

