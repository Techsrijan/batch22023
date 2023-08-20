'''
types of methods in class
1. instance method ---which accepts self as argument
2. class method -- which accepts cls as argument
3. static method - which accepts no argument
'''

class StudentData:
    school='techsrijan'
    # instance method
    def getmarks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        return self.m1+self.m2+self.m3

    @classmethod
    def getSchoolname(cls):
        return cls.school

    @staticmethod
    def msg():
        print("I will run ==how")

StudentData.msg()
print(StudentData.getSchoolname())
s=StudentData()
print(s.getmarks(10,20,30))
#print(StudentData.getSchoolname(s))