n=int(input("Enter any number"))
fact=1
# for i in range(1,n+1):
#     fact=fact*i

for i in range(n,1,-1):
    fact = fact * i

print(fact)