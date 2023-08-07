num=int(input("enter the any no"))
sum=0
mul=1
while num>0:
    a=num%10
    sum=sum+a
    mul=mul*a
    num=num//10

print("sum=",sum)
print("mul=",mul)