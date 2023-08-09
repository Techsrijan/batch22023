try:
    print("Fridge is open")
    a = int(input("enter first number"))
    b = int(input("enter Second number"))
    div=a/b
    print("Div=",div)

except ValueError:
    print("you have entered a charatcter")

except ZeroDivisionError:
    print("second number can not be zero")

except Exception:
    print("something Went Wrong")


finally:  #always runs
    print("Fridge is closed")

