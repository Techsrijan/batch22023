class Car:
    wheel=4    # class varibale
    def __init__(self):
        self.mil=33         #instance varibale -inside function
        self.name='Toyta'

c=Car()
c2=Car()
#c.car_info(25,'Maruti Wagnor')
print(c.mil,c.name,c.wheel)

Car.wheel=8
c2.mil=500
#c2.name='Tata Nexon'
print(c2.mil,c2.name,c2.wheel)

print(c.mil,c.name,c.wheel)