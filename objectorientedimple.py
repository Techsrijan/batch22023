class Student:
    def student_info(self,name,age):
        self.name=name
        self.age=age
        print("student Detail")
        print("Name=",self.name," ","Age=",self.age)

    def msg(self):
        print("This is student class")



s=Student()   # s is the oject of student class
#Student.student_info(s)
s.msg()
s.student_info('rohit',25)

