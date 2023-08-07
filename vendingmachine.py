n=int(input("how many toffee you want"))
stock=15
i=1
while i<=n:
    if i<=stock:
        print("collect toffe=",i)

    else:
        print("Out of stock")
        break
    i=i+1
else:
    print("thank u please visit again")