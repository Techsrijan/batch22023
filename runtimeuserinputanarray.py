from array import *

arr=array('i',[])  #empty array

num=int(input("How many students u have"))
print(num)

for i in range(num):
    print("enter the marks of=",i+1," student")
    marks=int(input())
    arr.append(marks)

print(arr)

max=arr[0]

for i in range(num):
    if arr[i]>max:
        max=arr[i]

print("max=",max)

min=arr[0]

for i in range(num):
    if arr[i]<min:
        min=arr[i]

print("min=",min)

search=int(input("entert the marks u want to find"))
for i in range(num):
    if arr[i]==search:
        print("Item found at location=",i+1)
        break
else:
    print("item Not Found")
