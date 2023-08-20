class Room:  #parent -area
    def area(self,l,b):
        self.l=l
        self.b=b
        area=self.l*self.b
        print("Area=",area)


class GuestRoom(Room):  #child -msg, area
    def msg(self):
        print("this is guest Room")


#r=Room()
#r.area(40,69)
g=GuestRoom()
g.msg()
g.area(40,50)
