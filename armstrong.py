num=int(input("enter the any  3 digit number no"))
sum=0
orig=num
while num>0:
    a=num%10
    sum=sum+a*a*a

    num=num//10

print("sum=",sum)
print("num=",num)
if sum==orig:
    print("armstrong number")
else:
    print("not armstrong")

